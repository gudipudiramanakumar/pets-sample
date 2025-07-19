<script lang="ts">
    import { onMount } from "svelte";

    interface Dog {
        id: number;
        name: string;
        breed: string;
        status: string;
    }

    interface Breed {
        id: number;
        name: string;
    }

    export let dogs: Dog[] = [];
    let loading = true;
    let error: string | null = null;
    let breeds: Breed[] = [];
    let selectedBreed = '';
    let selectedStatus = '';

    const fetchBreeds = async () => {
        try {
            const response = await fetch('/api/breeds');
            if(response.ok) {
                breeds = await response.json();
            }
        } catch (err) {
            console.error('Failed to fetch breeds:', err);
        }
    };

    const fetchDogs = async () => {
        loading = true;
        try {
            const params = new URLSearchParams();
            if (selectedBreed) params.append('breed', selectedBreed);
            if (selectedStatus) params.append('status', selectedStatus);
            
            const response = await fetch(`/api/dogs?${params.toString()}`);
            if(response.ok) {
                dogs = await response.json();
            } else {
                error = `Failed to fetch data: ${response.status} ${response.statusText}`;
            }
        } catch (err) {
            error = `Error: ${err instanceof Error ? err.message : String(err)}`;
        } finally {
            loading = false;
        }
    };

    const handleFilterChange = () => {
        fetchDogs();
    };

    onMount(() => {
        fetchBreeds();
        fetchDogs();
    });
</script>

<div>
    <h2 class="text-2xl font-medium mb-6 text-slate-100">Available Dogs</h2>
    
    <!-- Filters -->
    <div class="mb-6 flex flex-wrap gap-4">
        <div class="flex flex-col">
            <label for="breed-filter" class="text-sm text-slate-300 mb-2">Filter by Breed</label>
            <select 
                id="breed-filter"
                bind:value={selectedBreed} 
                on:change={handleFilterChange}
                class="bg-slate-800 border border-slate-600 text-slate-100 rounded-lg px-3 py-2 focus:border-blue-500 focus:outline-none"
            >
                <option value="">All Breeds</option>
                {#each breeds as breed}
                    <option value={breed.name}>{breed.name}</option>
                {/each}
            </select>
        </div>
        
        <div class="flex flex-col">
            <label for="status-filter" class="text-sm text-slate-300 mb-2">Availability</label>
            <select 
                id="status-filter"
                bind:value={selectedStatus} 
                on:change={handleFilterChange}
                class="bg-slate-800 border border-slate-600 text-slate-100 rounded-lg px-3 py-2 focus:border-blue-500 focus:outline-none"
            >
                <option value="">All Dogs</option>
                <option value="AVAILABLE">Available for Adoption</option>
                <option value="ADOPTED">Adopted</option>
                <option value="PENDING">Pending Adoption</option>
            </select>
        </div>
    </div>
    
    {#if loading}
        <!-- loading animation -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {#each Array(6) as _, i}
                <div class="bg-slate-800/60 backdrop-blur-sm rounded-xl overflow-hidden shadow-lg border border-slate-700/50">
                    <div class="p-6">
                        <div class="animate-pulse">
                            <div class="h-6 bg-slate-700 rounded w-3/4 mb-3"></div>
                            <div class="h-4 bg-slate-700 rounded w-1/2 mb-4"></div>
                            <div class="h-4 bg-slate-700 rounded w-1/4 mt-6"></div>
                        </div>
                    </div>
                </div>
            {/each}
        </div>
    {:else if error}
        <!-- error display -->
        <div class="text-center py-12 bg-slate-800/50 backdrop-blur-sm rounded-xl border border-slate-700">
            <p class="text-red-400">{error}</p>
        </div>
    {:else if dogs.length === 0}
        <!-- no dogs found -->
        <div class="text-center py-12 bg-slate-800/50 backdrop-blur-sm rounded-xl border border-slate-700">
            <p class="text-slate-300">No dogs match the current filters.</p>
        </div>
    {:else}
        <!-- dog list -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {#each dogs as dog (dog.id)}
                <a 
                    href={`/dog/${dog.id}`} 
                    class="group block bg-slate-800/60 backdrop-blur-sm rounded-xl overflow-hidden shadow-lg border border-slate-700/50 hover:border-blue-500/50 hover:shadow-blue-500/10 hover:shadow-xl transition-all duration-300 hover:translate-y-[-6px]"
                >
                    <div class="p-6 relative">
                        <div class="absolute inset-0 bg-gradient-to-r from-blue-600/10 to-purple-600/5 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                        <div class="relative z-10">
                            <h3 class="text-xl font-semibold text-slate-100 mb-2 group-hover:text-blue-400 transition-colors">{dog.name}</h3>
                            <p class="text-slate-400 mb-2">{dog.breed}</p>
                            <span class="inline-block px-2 py-1 text-xs rounded-full {dog.status === 'AVAILABLE' ? 'bg-green-500/20 text-green-400' : dog.status === 'ADOPTED' ? 'bg-red-500/20 text-red-400' : 'bg-yellow-500/20 text-yellow-400'}">{dog.status}</span>
                            <div class="mt-4 text-sm text-blue-400 font-medium flex items-center">
                                <span>View details</span>
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-1 transform transition-transform duration-300 group-hover:translate-x-2" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                                </svg>
                            </div>
                        </div>
                    </div>
                </a>
            {/each}
        </div>
    {/if}
</div>