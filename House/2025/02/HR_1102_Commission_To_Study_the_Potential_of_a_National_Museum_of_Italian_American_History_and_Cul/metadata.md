# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1102?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1102
- Title: Commission To Study the Potential of a National Museum of Italian American History and Culture Act
- Congress: 119
- Bill type: HR
- Bill number: 1102
- Origin chamber: House
- Introduced date: 2025-02-06
- Update date: 2025-12-10T09:06:23Z
- Update date including text: 2025-12-10T09:06:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-06: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-06 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-06: Introduced in House

## Actions

- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-06 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1102",
    "number": "1102",
    "originChamber": "House",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "S001201",
        "district": "3",
        "firstName": "Thomas",
        "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
        "lastName": "Suozzi",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Commission To Study the Potential of a National Museum of Italian American History and Culture Act",
    "type": "HR",
    "updateDate": "2025-12-10T09:06:23Z",
    "updateDateIncludingText": "2025-12-10T09:06:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-02-06T15:04:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-06T15:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "OH"
    },
    {
      "bioguideId": "A000369",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Amodei",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "NV"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CT"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "NY"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "OR"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "PA"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "NY"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley [R-WV-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "WV"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "DE"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "PA"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "OH"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NY"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "MD"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "MN"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "MI"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NJ"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "MA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NH"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "OH"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "NJ"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "WA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "NY"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "AL"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NC"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NJ"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CA"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "NY"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "TN"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "NY"
    },
    {
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "OH"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "CO"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "NE"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "NY"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "AL"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "AS"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "CA"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "GU"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "PA"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1102ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1102\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 6, 2025 Mr. Suozzi (for himself, Mr. Rulli , Mr. Amodei of Nevada , Ms. DeLauro , Mr. Panetta , Mr. Garbarino , Mr. Lawler , Ms. Bonamici , Mr. Peters , and Mr. Deluzio ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on House Administration , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish the Commission to Study the Potential Creation of a National Museum of Italian American History and Culture, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Commission To Study the Potential of a National Museum of Italian American History and Culture Act .\n#### 2. Establishment of Commission\n##### (a) In General\nThere is established the Commission to Study the Potential Creation of a National Museum of Italian American History and Culture (in this Act referred to as the Commission ).\n##### (b) Membership\nThe Commission shall be composed of 8 members, of whom\u2014\n**(1)**\n2 members shall be appointed by the majority leader of the Senate;\n**(2)**\n2 members shall be appointed by the Speaker of the House of Representatives;\n**(3)**\n2 members shall be appointed by the minority leader of the Senate; and\n**(4)**\n2 members shall be appointed by the minority leader of the House of Representatives.\n##### (c) Qualifications\nMembers of the Commission shall be appointed to the Commission from among individuals, or representatives of institutions or entities, who possess\u2014\n**(1)**\na demonstrated commitment to the research, study, or promotion of Italian American history, art, political or economic status, or culture;\n**(2)**\nexpertise or experience in\u2014\n**(A)**\nmuseum administration;\n**(B)**\nfundraising for nonprofit or cultural institutions;\n**(C)**\nthe study and teaching of Italian American history;\n**(D)**\nstudying the issue of the representation of Italian Americans in art, life, history, and culture at the Smithsonian Institution; or\n**(E)**\npublic or elected service that is extensive;\n**(3)**\nexperience in the administration of, or the planning for, the establishment of, museums; or\n**(4)**\nexperience in the planning, design, or construction of museum facilities.\n##### (d) Deadline for initial appointment\nNot later than the date that is 90 days after the date of enactment of this Act, the initial members of the Commission shall be appointed under subsection (b).\n##### (e) Vacancies\nA vacancy in the Commission\u2014\n**(1)**\nshall not affect the powers of the Commission; and\n**(2)**\nshall be filled in the same manner as the original appointment was made under subsection (b).\n##### (f) Chairperson\nThe Commission shall, by majority vote of all of the members, select 1 member of the Commission to serve as the Chairperson of the Commission.\n##### (g) Prohibition\nNo employee of the Federal Government may serve as a member of the Commission.\n#### 3. Duties of the Commission\n##### (a) Reports\n**(1) Plan of action**\nThe Commission shall submit to the President and Congress a report containing the recommendations of the Commission with respect to a plan of action regarding the feasibility of establishing and maintaining a National Museum of Italian American History and Culture in Washington, D.C., and the environs of such museum (in this Act referred to as the Museum ).\n**(2) Report on issues**\nThe Commission shall submit to the President and Congress a report that addresses the following:\n**(A)**\nThe availability and cost of collections to be acquired and housed in the Museum.\n**(B)**\nThe impact of the Museum on existing Italian American history-related museums.\n**(C)**\nThe development of criteria, in consultation with the Smithsonian Institution, for evaluating possible locations for the Museum in Washington, D.C., and the environs of such Museum.\n**(D)**\nThe feasibility of the Museum becoming part of the Smithsonian Institution, taking into account the potential impact of the Museum on the Smithsonian\u2019s existing facilities maintenance backlog, collections storage needs, and identified construction or renovation costs for new or existing museums.\n**(E)**\nThe governance and organizational structure from which the Museum should operate.\n**(F)**\nBest practices for engaging Italian Americans in the development and design of the Museum.\n**(G)**\nThe cost of constructing, operating, and maintaining the Museum.\n**(3) Deadline**\nNot later than the date that is 18 months after the date of the first meeting of the Commission, the Commission shall submit the reports required under paragraphs (1) and (2).\n##### (b) Fundraising plan\n**(1) In general**\nThe Commission shall develop a fundraising plan that shall address the ability to support the establishment, operation, and maintenance of the Museum through contributions from the public.\n**(2) Considerations**\nIn developing the fundraising plan under paragraph (1), the Commission shall consider issues relating to funding the operations and maintenance of the Museum in perpetuity without reliance on appropriations of Federal funds.\n**(3) Independent review**\n**(A) In general**\nThe Commission shall obtain an independent review of the viability of the plan developed under paragraph (1).\n**(B) Contents**\nThe independent review under subparagraph (A) shall include an analysis as to whether the plan is able to achieve the level of resources necessary to fund the construction of the Museum and the operations and maintenance of the Museum in perpetuity without reliance on appropriations of Federal funds.\n**(4) Submission**\nThe Commission shall submit to the Committees on House Administration, Natural Resources, and Appropriations of the House of Representatives and the Committees on Rules and Administration, Energy and Natural Resources, and Appropriations of the Senate the plan developed under paragraph (1) and the review conducted under paragraph (3).\n##### (c) Legislation to carry out plan of action\nBased on the recommendations contained in the report submitted under paragraphs (1) and (2) of subsection (a), the Commission shall submit for consideration to the Committees on House Administration, Natural Resources, and Appropriations of the House of Representatives and the Committees on Rules and Administration, Energy and Natural Resources, and Appropriations of the Senate recommendations for a legislative plan of action on the feasibility of establishing and constructing the Museum.\n##### (d) National conference\nNot later than 18 months after the date on which the initial members of the Commission are appointed under section 2(b), the Commission may, in carrying out the duties of the Commission under this section, convene a national conference relating to the Museum, to be comprised of individuals committed to the advancement of the life, art, history, and culture of Italian Americans.\n#### 4. Administrative Provisions\n##### (a) Compensation\n**(1) In general**\nA member of the Commission\u2014\n**(A)**\nshall not be considered to be a Federal employee for any purpose other than for purposes of chapter 81 of title 5, United States Code (relating to compensation for injury) and sections 2671 through 2680 of title 28, United States Code (relating to tort claims), except that each such individual shall be\u2014\n**(i)**\nrequired to file an annual financial disclosure under chapter 131 of title 5, United States Code; and\n**(ii)**\nconsidered to be a Federal employee for purposes of sections 201 and 208 of title 18, United States Code; and\n**(B)**\nshall serve without pay.\n**(2) Travel expenses**\nA member of the Commission shall be allowed a per diem allowance for travel expenses, at rates consistent with those authorized under subchapter I of chapter 57 of title 5, United States Code.\n**(3) Gifts, bequests, and devises**\nThe Commission may solicit, accept, use, and dispose of gifts, bequests, or devises of money, services, or real or personal property for the purpose of aiding or facilitating the work of the Commission.\n**(4) Federal advisory committee act**\nThe Commission shall not be subject to chapter 10 of title 5, United States Code.\n##### (b) Termination\nThe Commission shall terminate on the date that is 30 days after the date on which the final versions of the reports required under section 3 are submitted.\n##### (c) Funding\n**(1) In general**\nThe Commission shall be solely responsible for acceptance of contributions for, and payment of the expenses of, the Commission.\n**(2) Prohibition**\nNo Federal funds may be obligated to carry out this Act.\n##### (d) Director and Staff of commission\n**(1) Director and staff**\n**(A) In general**\nThe Commission may employ and compensate an executive director and any other additional personnel that are necessary to enable the Commission to perform the duties of the Commission.\n**(B) Rates of pay**\nRates of pay for persons employed under subparagraph (A) shall be consistent with the rates of pay allowed for employees of a temporary organization under section 3161 of title 5, United States Code.\n**(2) Not Federal employees**\nAny individual employed under this subsection shall not be considered a Federal employee for any purpose other than for purposes of chapter 81 of title 5, United States Code (relating to compensation for injury) and sections 2671 through 2680 of title 28, United States Code (relating to tort claims), except that each such individual shall be\u2014\n**(A)**\nrequired to file an annual financial disclosure under chapter 131 of title 5, United States Code; and\n**(B)**\nconsidered to be a Federal employee for purposes of sections 201 and 208 of title 18, United States Code.\n**(3) Technical assistance**\n**(A) In general**\nSubject to subparagraph (B), on request of the Commission, the head of a Federal agency may provide technical assistance to the Commission.\n**(B) Prohibition**\nNo Federal employees may be detailed to the Commission.",
      "versionDate": "2025-02-06",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Arts, Culture, Religion",
        "updateDate": "2025-03-11T18:33:08Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1102ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Commission To Study the Potential of a National Museum of Italian American History and Culture Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:59:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Commission To Study the Potential of a National Museum of Italian American History and Culture Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-10T12:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Commission to Study the Potential Creation of a National Museum of Italian American History and Culture, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-10T12:33:36Z"
    }
  ]
}
```
