# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1585?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1585
- Title: Conrad State 30 and Physician Access Reauthorization Act
- Congress: 119
- Bill type: HR
- Bill number: 1585
- Origin chamber: House
- Introduced date: 2025-02-25
- Update date: 2026-04-21T08:06:05Z
- Update date including text: 2026-04-21T08:06:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-25: Introduced in House

## Actions

- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1585",
    "number": "1585",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "V000129",
        "district": "22",
        "firstName": "David",
        "fullName": "Rep. Valadao, David G. [R-CA-22]",
        "lastName": "Valadao",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Conrad State 30 and Physician Access Reauthorization Act",
    "type": "HR",
    "updateDate": "2026-04-21T08:06:05Z",
    "updateDateIncludingText": "2026-04-21T08:06:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T15:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "NE"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "IL"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "TX"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "FL"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "KS"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "GA"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "GA"
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
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "IL"
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
      "sponsorshipDate": "2025-03-05",
      "state": "WA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "NY"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "PA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NY"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "PA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NY"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CA"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "AZ"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "DE"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "NC"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "FL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "NY"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "WA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "MN"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "CA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "HI"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NY"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "MI"
    },
    {
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "NC"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "MI"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "NJ"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "FL"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "NC"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "IL"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "CA"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "VA"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "TX"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "CO"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "CA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "RI"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "OR"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "TX"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CO"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "VA"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "AZ"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "NJ"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "NM"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "VA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "NV"
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
      "sponsorshipDate": "2025-09-30",
      "state": "MI"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "NY"
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
      "sponsorshipDate": "2025-10-08",
      "state": "MA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "DC"
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
      "sponsorshipDate": "2025-10-17",
      "state": "NY"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "NM"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
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
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "ME"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
      "state": "IL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1585ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1585\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2025 Mr. Valadao (for himself, Mr. Bacon , Mr. Schneider , and Ms. Garcia of Texas ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide incentives to physicians to practice in rural and medically underserved communities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Conrad State 30 and Physician Access Reauthorization Act .\n#### 2. Conrad State 30 program\n##### (a) Extension\nSection 220(c) of the Immigration and Nationality Technical Corrections Act of 1994 ( Public Law 103\u2013416 ; 8 U.S.C. 1182 note) is amended by striking September 30, 2015 and inserting on the date that is 3 years after the date of the enactment of the Conrad State 30 and Physician Access Reauthorization Act .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect as if enacted on September 30, 2018.\n#### 3. Retaining physicians who have practiced in medically underserved communities\nSection 201(b)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1151(b)(1) ) is amended by adding at the end the following:\n(F) (i) Alien physicians who have completed service requirements of a waiver requested under section 203(b)(2)(B)(ii), including\u2014 (I) alien physicians who completed such service before the date of the enactment of the Conrad State 30 and Physician Access Act ; and (II) the spouse or children of an alien physician described in subclause (I). (ii) Nothing in this subparagraph may be construed\u2014 (I) to prevent the filing of a petition with the Secretary of Homeland Security for classification under section 204(a) or the filing of an application for adjustment of status under section 245 by an alien physician described in this subparagraph before the date by which such alien physician has completed the service described in section 214(l) or worked full-time as a physician for an aggregate of 5 years at the location identified in the section 214(l) waiver or in an area or areas designated by the Secretary of Health and Human Services as having a shortage of health care professionals; or (II) to permit the Secretary of Homeland Security to grant a petition or application described in subclause (I) until the alien has satisfied all of the requirements of the waiver received under section 214(l). .\n#### 4. Employment protections for physicians\n##### (a) Exceptions to 2-Year foreign residency requirement\nSection 214(l)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1184(l)(1) ) is amended\u2014\n**(1)**\nin the matter preceding subparagraph (A), by striking Attorney General and inserting Secretary of Homeland Security ;\n**(2)**\nin subparagraph (A), by striking Director of the United States Information Agency and inserting Secretary of State ;\n**(3)**\nin subparagraph (B), by inserting , except as provided in paragraphs (7) and (8) before the semicolon at the end;\n**(4)**\nin subparagraph (C), by striking clauses (i) and (ii) and inserting the following:\n(i) the alien demonstrates a bona fide offer of full-time employment at a health facility or health care organization, which employment has been determined by the Secretary of Homeland Security to be in the public interest; and (ii) the alien\u2014 (I) has accepted employment with the health facility or health care organization in a geographic area or areas which are designated by the Secretary of Health and Human Services as having a shortage of health care professionals; (II) begins employment by the later of the date that is\u2014 (aa) 120 days after receiving such waiver; (bb) 120 days after completing graduate medical education or training under a program approved pursuant to section 212(j)(1); or (cc) 120 days after receiving nonimmigrant status or employment authorization, if the alien or the alien\u2019s employer petitions for such nonimmigrant status or employment authorization not later than 120 days after the date on which the alien completes his or her graduate medical education or training under a program approved pursuant to section 212(j)(1); and (III) agrees to continue to work for a total of not less than 3 years in the status authorized for such employment under this subsection, except as provided in paragraph (8). ; and\n**(5)**\nin subparagraph (D), in the matter preceding clause (i), by inserting (except as provided in paragraph (8)) after 3 years .\n##### (b) Allowable visa status for physicians fulfilling waiver requirements in medically underserved areas\nSection 214(l)(2)(A) of such Act ( 8 U.S.C. 1184(l)(2)(A) ) is amended to read as follows:\n(A) Upon the request of an interested Federal agency or an interested State agency for recommendation of a waiver under this section by a physician who is maintaining valid nonimmigrant status under section 101(a)(15)(J) and a favorable recommendation by the Secretary of State, the Secretary of Homeland Security may change the status of such physician to any status authorized for employment under this Act. The numerical limitations contained in subsection (g)(1)(A) shall not apply to any alien whose status is changed under this subparagraph. .\n##### (c) Violation of agreements\nSection 214(l)(3)(A) of such Act ( 8 U.S.C. 1184(l)(3)(A) ) is amended by inserting substantial requirement of an before agreement entered into .\n##### (d) Physician employment in underserved areas\nSection 214(l) of such Act, as amended by this section, is further amended by adding at the end the following:\n(4) (A) If an interested State agency denies an application for a waiver under paragraph (1)(B) from a physician pursuing graduate medical education or training pursuant to section 101(a)(15)(J) because the State has requested the maximum number of waivers permitted for that fiscal year, the physician\u2019s nonimmigrant status shall be extended for up to 6 months if the physician agrees to seek a waiver under this subsection (except for paragraph (1)(D)(ii)) to work for an employer described in paragraph (1)(C) in a State that has not yet requested the maximum number of waivers. (B) Such physician shall be authorized to work only for the employer referred to in subparagraph (A) during the period beginning on the date on which a new waiver application is filed with such State and ending on the earlier of\u2014 (i) the date on which the Secretary of Homeland Security denies such waiver; or (ii) the date on which the Secretary approves an application for change of status under paragraph (2)(A) pursuant to the approval of such waiver. .\n##### (e) Contract requirements\nSection 214(l) of such Act, as amended by this section, is further amended by adding at the end the following:\n(5) An alien granted a waiver under paragraph (1)(C) shall enter into an employment agreement with the contracting health facility or health care organization that\u2014 (A) specifies the maximum number of on-call hours per week (which may be a monthly average) that the alien will be expected to be available and the compensation the alien will receive for on-call time; (B) specifies\u2014 (i) whether the contracting facility or organization\u2014 (I) has secured medical malpractice liability protection for the alien under section 224(g) of the Public Health Service Act ( 42 U.S.C. 233(g) ); or (II) will pay the alien\u2019s malpractice insurance premiums; (ii) whether the employer will provide malpractice insurance for the alien; and (iii) the amount of such liability protection that will be provided; (C) describes all of the work locations that the alien will work and includes a statement that the contracting facility or organization will not add additional work locations without the approval of the Federal agency or State agency that requested the waiver; and (D) does not include a non-compete provision. (6) An alien granted a waiver under this subsection whose employment relationship with a health facility or health care organization terminates under paragraph (1)(C)(ii) during the 3-year service period required under paragraph (1) shall be considered to be maintaining lawful status in an authorized period of stay during the 120-day period referred to in items (aa) and (bb) of subclause (III) of paragraph (1)(C)(ii) or the 45-day period referred to in subclause (III)(cc) of such paragraph. .\n##### (f) Recapturing waiver slots lost to other States\nSection 214(l) of such Act, as amended by this section, is further amended by adding at the end the following:\n(7) If a recipient of a waiver under this subsection terminates the recipient\u2019s employment with a health facility or health care organization pursuant to paragraph (1)(C)(ii), including termination of employment because of circumstances described in paragraph (1)(C)(ii)(III), and accepts new employment with such a facility or organization in a different State, the State from which the alien is departing may be accorded an additional waiver by the Secretary of State for use in the fiscal year in which the alien\u2019s employment was terminated. .\n##### (g) Exception to 3-Year work requirement\nSection 214(l) of such Act, as amended by this section, is further amended by adding at the end the following:\n(8) The 3-year work requirement set forth in subparagraphs (C) and (D) of paragraph (1) shall not apply if\u2014 (A) (i) the Secretary of Homeland Security determines that extenuating circumstances, including violations by the employer of the employment agreement with the alien or of labor and employment laws, exist that justify a lesser period of employment at such facility or organization; and (ii) the alien demonstrates, not later than 120 days after the employment termination date (unless the Secretary determines that extenuating circumstances would justify an extension), another bona fide offer of employment at a health facility or health care organization in a geographic area or areas which are designated by the Secretary of Health and Human Services as having a shortage of health care professionals, for the remainder of such 3-year period; (B) (i) the interested State agency that requested the waiver attests that extenuating circumstances, including violations by the employer of the employment agreement with the alien or of labor and employment laws, exist that justify a lesser period of employment at such facility or organization; and (ii) the alien demonstrates, not later than 120 days after the employment termination date (unless the Secretary determines that extenuating circumstances would justify an extension), another bona fide offer of employment at a health facility or health care organization in a geographic area or areas which are designated by the Secretary of Health and Human Services as having a shortage of health care professionals, for the remainder of such 3-year period; or (C) the alien\u2014 (i) elects not to pursue a determination of extenuating circumstances pursuant to subclause (A) or (B); (ii) terminates the alien\u2019s employment relationship with the health facility or health care organization at which the alien was employed; (iii) demonstrates, not later than 45 days after the employment termination date, another bona fide offer of employment at a health facility or health care organization in a geographic area or areas, in the State that requested the alien\u2019s waiver, which are designated by the Secretary of Health and Human Services as having a shortage of health care professionals; and (iv) agrees to be employed for the remainder of such 3-year period, and 1 additional year for each termination under clause (ii). .\n#### 5. Allotment of Conrad 30 waivers\n##### (a) In general\nSection 214(l) of the Immigration and Nationality Act ( 8 U.S.C. 1184(l) ), as amended by section 4, is further amended by adding at the end the following:\n(9) (A) (i) All States shall be allotted a total of 35 waivers under paragraph (1)(B) for a fiscal year if 90 percent of the waivers available to the States receiving at least 5 waivers were used in the previous fiscal year. (ii) When an allotment occurs under clause (i), all States shall be allotted an additional 5 waivers under paragraph (1)(B) for each subsequent fiscal year if 90 percent of the waivers available to the States receiving at least 5 waivers were used in the previous fiscal year. If the States are allotted 45 or more waivers for a fiscal year, the States will only receive an additional increase of 5 waivers the following fiscal year if 95 percent of the waivers available to the States receiving at least 1 waiver were used in the previous fiscal year. (B) Any increase in allotments under subparagraph (A) shall be maintained indefinitely, unless in a fiscal year, the total number of such waivers granted is 5 percent lower than in the last year in which there was an increase in the number of waivers allotted pursuant to this paragraph, in which case\u2014 (i) the number of waivers allotted shall be decreased by 5 for all States beginning in the next fiscal year; and (ii) each additional 5 percent decrease in such waivers granted from the last year in which there was an increase in the allotment, shall result in an additional decrease of 5 waivers allotted for all States, provided that the number of waivers allotted for all States shall not drop below 30. .\n##### (b) Academic medical centers\nSection 214(l)(1)(D) of such Act ( 8 U.S.C. 1184(l)(1)(D) ), as amended by section 4(a)(5), is further amended\u2014\n**(1)**\nin clause (ii), by striking and at the end;\n**(2)**\nin clause (iii), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(iv) in the case of a request by an interested State agency\u2014 (I) the head of such agency determines that the alien is to practice medicine in, or be on the faculty of a residency program at, an academic medical center (as that term is defined in section 411.355(e)(2) of title 42, Code of Federal Regulations, or similar successor regulation), without regard to whether such facility is located within an area designated by the Secretary of Health and Human Services as having a shortage of health care professionals; and (II) the head of such agency determines that\u2014 (aa) the alien physician\u2019s work is in the public interest; and (bb) the grant of such waiver would not cause the number of the waivers granted on behalf of aliens for such State for a fiscal year (within the limitation in subparagraph (B) and subject to paragraph (6)) in accordance with the conditions of this clause to exceed 3. .\n#### 6. Amendments to the procedures, definitions, and other provisions related to physician immigration\n##### (a) Dual intent for physicians seeking graduate medical training\nSection 214(b) of the Immigration and Nationality Act ( 8 U.S.C. 1184(b) ) is amended by striking (other than a nonimmigrant described in subparagraph (L) or (V) of section 101(a)(15), and other than a nonimmigrant described in any provision of section 101(a)(15)(H)(i) except subclause (b1) of such section) and inserting (other than a nonimmigrant described in subparagraph (L) or (V) of section 101(a)(15), a nonimmigrant described in any provision of section 101(a)(15)(H)(i) (except subclause (b1) of such section), and an alien coming to the United States to receive graduate medical education or training described in section 212(j) or to take examinations required to receive graduate medical education or training described in section 212(j)) .\n##### (b) Physician national interest waiver clarifications\n**(1) Practice and geographic area**\nSection 203(b)(2)(B)(ii)(I) of the Immigration and Nationality Act ( 8 U.S.C. 1153(b)(2)(B)(ii)(I) ) is amended by striking items (aa) and (bb) and inserting the following:\n(aa) the alien physician agrees to work on a full-time basis practicing primary care, specialty medicine, or a combination thereof, in an area or areas designated by the Secretary of Health and Human Services as having a shortage of health care professionals, or at a health care facility under the jurisdiction of the Secretary of Veterans Affairs; or (bb) the alien physician is pursuing such waiver based upon service at a facility or facilities that serve patients who reside in a geographic area or areas designated by the Secretary of Health and Human Services as having a shortage of health care professionals (without regard to whether such facility or facilities are located within such an area) and a Federal agency, or a local, county, regional, or State department of public health determines the alien physician\u2019s work was or will be in the public interest. .\n**(2) Five-year service requirement**\nSection 203(b)(2)(B)(ii) of the Immigration and Nationality Act (8 U.S.C. 1153(B)(ii)) is amended\u2014\n**(A)**\nby moving subclauses (II), (III), and (IV) 4 ems to the left; and\n**(B)**\nin subclause (II)\u2014\n**(i)**\nby inserting (aa) after (II) ; and\n**(ii)**\nby adding at the end the following:\n(bb) The 5-year service requirement under item (aa) shall begin on the date on which the alien physician begins work in the shortage area in any legal status and not on the date on which an immigrant visa petition is filed or approved. Such service shall be aggregated without regard to when such service began and without regard to whether such service began during or in conjunction with a course of graduate medical education. (cc) An alien physician shall not be required to submit an employment contract with a term exceeding the balance of the 5-year commitment yet to be served or an employment contract dated within a minimum time period before filing a visa petition under this subsection. (dd) An alien physician shall not be required to file additional immigrant visa petitions upon a change of work location from the location approved in the original national interest immigrant petition. .\n##### (c) Technical clarification regarding advanced degree for physicians\nSection 203(b)(2)(A) of the Immigration and Nationality Act ( 8 U.S.C. 1153(b)(2)(A) ) is amended by adding at the end the following: An alien physician holding a foreign medical degree that has been deemed sufficient for acceptance by an accredited United States medical residency or fellowship program is a member of the professions holding an advanced degree or its equivalent. .\n##### (d) Short-Term work authorization for physicians completing their residencies\n**(1) In general**\nA physician completing graduate medical education or training described in section 212(j) of the Immigration and Nationality Act ( 8 U.S.C. 1182(j) ) as a nonimmigrant described in section 101(a)(15)(H)(i) of such Act ( 8 U.S.C. 1101(a)(15)(H)(i) )\u2014\n**(A)**\nshall have such nonimmigrant status automatically extended until October 1 of the fiscal year for which a petition for a continuation of such nonimmigrant status has been submitted in a timely manner and the employment start date for the beneficiary of such petition is October 1 of that fiscal year; and\n**(B)**\nshall be authorized to be employed incident to status during the period between the filing of such petition and October 1 of such fiscal year.\n**(2) Termination**\nThe physician\u2019s status and employment authorization shall terminate on the date that is 30 days after the date on which a petition described in paragraph (1)(A) is rejected, denied or revoked.\n**(3) Automatic extension**\nA physician\u2019s status and employment authorization will automatically extend to October 1 of the next fiscal year if all of the visas described in section 101(a)(15)(H)(i) of such Act that were authorized to be issued for the fiscal year have been issued.\n##### (e) Applicability of section 212( e ) to spouses and children of J\u20131 exchange visitors\nA spouse or child of an exchange visitor described in section 101(a)(15)(J) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(J) ) shall not be subject to the requirements under section 212(e) of such Act ( 8 U.S.C. 1182(e) ).\n#### 7. Annual Conrad State 30 J\u20131 Visa Waiver Program statistical report\nThe Director of U.S. Citizenship and Immigration Services shall submit an annual report to Congress and to the Department of Health and Human Services that identifies the number of aliens admitted during the most recently concluded fiscal year as a result of the Conrad State 30 J\u20131 Visa Waiver Program established under sections 212(e) and 214(l) of the Immigration and Nationality Act ( 8 U.S.C. 1182(e) and 1184(l)), disaggregated by State.",
      "versionDate": "2025-02-25",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-25",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "709",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Conrad State 30 and Physician Access Reauthorization Act",
      "type": "S"
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
        "name": "Immigration",
        "updateDate": "2025-03-18T14:04:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1585",
          "measure-number": "1585",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-25",
          "originChamber": "HOUSE",
          "update-date": "2026-01-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1585v00",
            "update-date": "2026-01-06"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Conrad State 30 and Physician Access Reauthorization Act</strong></p><p>This bill modifies the Conrad 30 Waiver program, which incentivizes qualified foreign physicians to serve in underserved communities. It also extends statutory authority for the program for three years from this bill's enactment.</p><p>Individuals coming to the United States under a J-1 nonimmigrant visa to receive medical training typically must leave the country and reside for two years abroad before being eligible to apply for an immigrant visa or permanent residence. The Conrad program waives this requirement for individuals who meet certain qualifications, including serving for a number of years at a health care facility in an underserved area.</p><p>The bill increases the number of waivers that a state may obtain each fiscal year from 30 to 35 if a certain number of waivers were used the previous year, and provides for further adjustments depending on demand.</p><p>A physician may be employed at an academic medical center to meet the Conrad program's employment requirements if the physician's work is in the public interest, even if the medical center is not in an underserved area.</p><p>Employment contracts for physicians under the Conrad program shall contain certain information, such as the maximum number of on-call hours per week the physician shall have to work.</p><p>Certain physicians (along with the physician's spouse and children) shall be exempt from the direct annual numerical limits on immigration, including those physicians that have met certain requirements related to visas for physicians to serve in underserved areas.</p>"
        },
        "title": "Conrad State 30 and Physician Access Reauthorization Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1585.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Conrad State 30 and Physician Access Reauthorization Act</strong></p><p>This bill modifies the Conrad 30 Waiver program, which incentivizes qualified foreign physicians to serve in underserved communities. It also extends statutory authority for the program for three years from this bill's enactment.</p><p>Individuals coming to the United States under a J-1 nonimmigrant visa to receive medical training typically must leave the country and reside for two years abroad before being eligible to apply for an immigrant visa or permanent residence. The Conrad program waives this requirement for individuals who meet certain qualifications, including serving for a number of years at a health care facility in an underserved area.</p><p>The bill increases the number of waivers that a state may obtain each fiscal year from 30 to 35 if a certain number of waivers were used the previous year, and provides for further adjustments depending on demand.</p><p>A physician may be employed at an academic medical center to meet the Conrad program's employment requirements if the physician's work is in the public interest, even if the medical center is not in an underserved area.</p><p>Employment contracts for physicians under the Conrad program shall contain certain information, such as the maximum number of on-call hours per week the physician shall have to work.</p><p>Certain physicians (along with the physician's spouse and children) shall be exempt from the direct annual numerical limits on immigration, including those physicians that have met certain requirements related to visas for physicians to serve in underserved areas.</p>",
      "updateDate": "2026-01-06",
      "versionCode": "id119hr1585"
    },
    "title": "Conrad State 30 and Physician Access Reauthorization Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Conrad State 30 and Physician Access Reauthorization Act</strong></p><p>This bill modifies the Conrad 30 Waiver program, which incentivizes qualified foreign physicians to serve in underserved communities. It also extends statutory authority for the program for three years from this bill's enactment.</p><p>Individuals coming to the United States under a J-1 nonimmigrant visa to receive medical training typically must leave the country and reside for two years abroad before being eligible to apply for an immigrant visa or permanent residence. The Conrad program waives this requirement for individuals who meet certain qualifications, including serving for a number of years at a health care facility in an underserved area.</p><p>The bill increases the number of waivers that a state may obtain each fiscal year from 30 to 35 if a certain number of waivers were used the previous year, and provides for further adjustments depending on demand.</p><p>A physician may be employed at an academic medical center to meet the Conrad program's employment requirements if the physician's work is in the public interest, even if the medical center is not in an underserved area.</p><p>Employment contracts for physicians under the Conrad program shall contain certain information, such as the maximum number of on-call hours per week the physician shall have to work.</p><p>Certain physicians (along with the physician's spouse and children) shall be exempt from the direct annual numerical limits on immigration, including those physicians that have met certain requirements related to visas for physicians to serve in underserved areas.</p>",
      "updateDate": "2026-01-06",
      "versionCode": "id119hr1585"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1585ih.xml"
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
      "title": "Conrad State 30 and Physician Access Reauthorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Conrad State 30 and Physician Access Reauthorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide incentives to physicians to practice in rural and medically underserved communities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:26Z"
    }
  ]
}
```
