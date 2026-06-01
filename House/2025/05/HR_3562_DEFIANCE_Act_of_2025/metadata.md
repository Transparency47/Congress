# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3562?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3562
- Title: DEFIANCE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3562
- Origin chamber: House
- Introduced date: 2025-05-21
- Update date: 2026-02-05T09:06:02Z
- Update date including text: 2026-02-05T09:06:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-21: Introduced in House

## Actions

- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3562",
    "number": "3562",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "O000172",
        "district": "14",
        "firstName": "Alexandria",
        "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
        "lastName": "Ocasio-Cortez",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "DEFIANCE Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-05T09:06:02Z",
    "updateDateIncludingText": "2026-02-05T09:06:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
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
      "actionDate": "2025-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T14:03:10Z",
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
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "FL"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "FL"
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
      "sponsorshipDate": "2025-05-21",
      "state": "PA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "MI"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "NY"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "CA"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "SC"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "OH"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "MD"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "CO"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "NJ"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
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
      "sponsorshipDate": "2025-06-25",
      "state": "PA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "NY"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "TX"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "NJ"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "NC"
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
      "sponsorshipDate": "2026-01-12",
      "state": "CA"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "OH"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "CA"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "AZ"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "FL"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "AZ"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "NJ"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "MI"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "PA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "DE"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "TX"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "FL"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "IN"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "OH"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "IL"
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
      "sponsorshipDate": "2026-01-21",
      "state": "DC"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "False",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "L000595",
      "district": "5",
      "firstName": "Julia",
      "fullName": "Rep. Letlow, Julia [R-LA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Letlow",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "LA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "SC"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "MA"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "FL"
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
      "sponsorshipDate": "2026-01-22",
      "state": "NC"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "IA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "NJ"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "MO"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "NV"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
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
      "sponsorshipDate": "2026-01-30",
      "state": "CA"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "NY"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "NC"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3562ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3562\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2025 Ms. Ocasio-Cortez (for herself, Ms. Lee of Florida , Mrs. Cammack , Mr. Deluzio , Mrs. Dingell , Mr. Lawler , Mr. Lieu , Ms. Mace , Mr. Miller of Ohio , Mr. Raskin , Ms. Pettersen , and Mr. Van Drew ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo improve rights to relief for individuals affected by non-consensual activities involving intimate digital forgeries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Disrupt Explicit Forged Images And Non-Consensual Edits Act of 2025 or the DEFIANCE Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nDigital forgeries, often called deepfakes, are synthetic images and videos that look realistic. The technology to create digital forgeries is now ubiquitous and easy to use. Hundreds of apps are available that can quickly generate digital forgeries without the need for any technical expertise.\n**(2)**\nDigital forgeries can be wholly fictitious but can also manipulate images of real people to depict sexually intimate conduct that did not occur. For example, some digital forgeries will paste the face of an individual onto the body of a real or fictitious individual who is nude or who is engaging in sexual activity. Another example is a photograph of an individual that is manipulated to digitally remove the clothing of the individual so that the person appears to be nude.\n**(3)**\nThe individuals depicted in such digital forgeries are profoundly harmed when the content is produced with intent to disclose, disclosed, or obtained without the consent of those individuals. These harms are not mitigated through labels or other information that indicates that the depiction is fake.\n**(4)**\nIt can be destabilizing to victims whenever those victims are depicted in intimate digital forgeries against their will, as the privacy of those victims is violated and the victims lose control over their likeness and identity.\n**(5)**\nVictims can feel helpless because the victims\u2014\n**(A)**\nmay not be able to determine who has created the content; and\n**(B)**\ndo not know how to prevent further disclosure of the intimate digital forgery or how to prevent more forgeries from being made.\n**(6)**\nVictims may be fearful of being in public out of concern that individuals the victims encounter have seen the digital forgeries. This leads to social rupture through the loss of the ability to trust, stigmatization, and isolation.\n**(7)**\nVictims of non-consensual, sexually intimate digital forgeries may experience depression, anxiety, and suicidal ideation. These victims may also experience the silencing effect in which the victims withdraw from online spaces and public discourse to avoid further abuse.\n**(8)**\nDigital forgeries are often used to\u2014\n**(A)**\nharass victims, interfering with their employment, education, reputation, or sense of safety; or\n**(B)**\ncommit extortion, sexual assault, domestic violence, and other crimes.\n**(9)**\nBecause of the harms caused by non-consensual, sexually intimate digital forgeries, such digital forgeries are considered to be a form of image-based sexual abuse.\n#### 3. Civil action relating to disclosure of intimate images\n##### (a) Definitions\nSection 1309 of the Consolidated Appropriations Act, 2022 ( 15 U.S.C. 6851 ) is amended\u2014\n**(1)**\nin the section heading, by inserting or nonconsensual activity involving digital forgeries after intimate images ; and\n**(2)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (2), by inserting competent, after conscious, ;\n**(B)**\nby striking paragraph (3);\n**(C)**\nby redesignating paragraph (4) as paragraph (3);\n**(D)**\nby redesignating paragraphs (5) and (6) as paragraphs (6) and (7), respectively;\n**(E)**\nby inserting after paragraph (3) the following:\n(4) Identifiable individual The term identifiable individual means an individual whose body appears in whole or in part in an intimate visual depiction or intimate digital forgery and who is identifiable by virtue of the individual\u2019s face, likeness, or other distinguishing characteristic, such as a unique birthmark or other recognizable feature, or from information displayed in connection with the intimate visual depiction or intimate digital forgery. (5) Intimate digital forgery (A) In general The term intimate digital forgery means any intimate visual depiction of an identifiable individual that\u2014 (i) falsely represents, in whole or in part\u2014 (I) the identifiable individual; or (II) the conduct or content that makes the visual depiction intimate; (ii) is created through the use of software, machine learning, artificial intelligence, or any other computer-generated or technological means, including by adapting, modifying, manipulating, or altering an authentic visual depiction; and (iii) is indistinguishable from an authentic visual depiction of the identifiable individual when viewed as a whole by a reasonable person. (B) Labels, disclosure, and context Any visual depiction described in subparagraph (A) constitutes an intimate digital forgery for purposes of this paragraph regardless of whether a label, information disclosed with the visual depiction, or the context or setting in which the visual depiction is disclosed states or implies that the visual depiction is not authentic. ; and\n**(F)**\nin paragraph (6)(A), as so redesignated\u2014\n**(i)**\nin clause (i), by striking or at the end;\n**(ii)**\nin clause (ii)\u2014\n**(I)**\nin subclause (I), by striking individual; and inserting individual; or ; and\n**(II)**\nby striking subclause (III); and\n**(iii)**\nby adding at the end the following:\n(iii) an identifiable individual engaging in sexually explicit conduct; and .\n##### (b) Civil action\nSection 1309(b) of the Consolidated Appropriations Act, 2022 ( 15 U.S.C. 6851(b) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking subparagraph (A) and inserting the following:\n(A) In general Except as provided in paragraph (5)\u2014 (i) an identifiable individual whose intimate visual depiction is disclosed, in or affecting interstate or foreign commerce or using any means or facility of interstate or foreign commerce, without the consent of the identifiable individual, where such disclosure was made by a person who knows or recklessly disregards that the identifiable individual has not consented to such disclosure, may bring a civil action against that person in an appropriate district court of the United States for relief as set forth in paragraph (3); (ii) an identifiable individual who is the subject of an intimate digital forgery may bring a civil action in an appropriate district court of the United States for relief as set forth in paragraph (3) against any person that knowingly produced or possessed the intimate digital forgery with intent to disclose it, knowingly disclosed the intimate digital forgery, or knowingly solicited and received the intimate digital forgery, if\u2014 (I) the identifiable individual did not consent to such production or possession with intent to disclose, disclosure, or solicitation and receipt; (II) the person knew or recklessly disregarded that the identifiable individual did not consent to such production or possession with intent to disclose, disclosure, or solicitation and receipt; and (III) such production or possession with intent to disclose, disclosure, or solicitation and receipt, is in or affects interstate or foreign commerce or uses any means or facility of interstate or foreign commerce; and (iii) an identifiable individual who is the subject of an intimate digital forgery may bring a civil action in an appropriate district court of the United States for relief as set forth in paragraph (3) against any person that knowingly produced the intimate digital forgery if\u2014 (I) the identifiable individual did not consent to such production; (II) the person knew or recklessly disregarded that the identifiable individual\u2014 (aa) did not consent to such production; and (bb) was harmed, or was reasonably likely to be harmed, by the production; and (III) such production is in or affects interstate or foreign commerce or uses any means or facility of interstate or foreign commerce. ; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nin the subparagraph heading, by inserting identifiable before individuals ; and\n**(ii)**\nby striking an individual who is under 18 years of age, incompetent, incapacitated, or deceased, the legal guardian of the individual and inserting an identifiable individual who is under 18 years of age, incompetent, incapacitated, or deceased, the legal guardian of the identifiable individual ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby inserting identifiable before individual ;\n**(ii)**\nby striking depiction and inserting intimate visual depiction or intimate digital forgery ; and\n**(iii)**\nby striking distribution and inserting disclosure, solicitation, or possession ; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nby inserting identifiable before individual ;\n**(ii)**\nby inserting or intimate digital forgery after depiction each place it appears; and\n**(iii)**\nby inserting , solicitation, or possession after disclosure ;\n**(3)**\nby redesignating paragraph (4) as paragraph (5);\n**(4)**\nby striking paragraph (3) and inserting the following:\n(3) Relief (A) In general In a civil action filed under this section, an identifiable individual may recover\u2014 (i) damages as provided under subparagraph (C); and (ii) the cost of the action, including reasonable attorney fees and other litigation costs reasonably incurred. (B) Punitive damages and other relief The court may, in addition to any other relief available at law, award punitive damages or order equitable relief, including a temporary restraining order, a preliminary injunction, or a permanent injunction ordering the defendant to delete, destroy, or cease to display or disclose the intimate visual depiction or intimate digital forgery. (C) Damages For purposes of subparagraph (A)(i), the identifiable individual may recover\u2014 (i) liquidated damages in the amount of\u2014 (I) $150,000; or (II) $250,000 if the conduct at issue in the claim was\u2014 (aa) committed in relation to actual or attempted sexual assault, stalking, or harassment of the identifiable individual by the defendant; or (bb) the direct and proximate cause of actual or attempted sexual assault, stalking, or harassment of the identifiable individual by any person; or (ii) actual damages sustained by the individual, which shall include any profits of the defendant that are attributable to the conduct at issue in the claim that are not otherwise taken into account in computing the actual damages. (D) Calculation of defendant\u2019s profit For purposes of subparagraph (C)(ii), to establish the defendant\u2019s profits, the identifiable individual shall be required to present proof only of the gross revenue of the defendant, and the defendant shall be required to prove the deductible expenses of the defendant and the elements of profit attributable to factors other than the conduct at issue in the claim. (4) Preservation of privacy In a civil action filed under this section, the court may issue an order to protect the privacy of a plaintiff, including by\u2014 (A) permitting the plaintiff to use a pseudonym; (B) requiring the parties to redact the personal identifying information of the plaintiff from any public filing, or to file such documents under seal; and (C) issuing a protective order for purposes of discovery, which may include an order indicating that any intimate visual depiction or intimate digital forgery shall remain in the care, custody, and control of the court. ;\n**(5)**\nin paragraph (5)(A), as so redesignated\u2014\n**(A)**\nby striking image and inserting visual depiction or intimate digital forgery ; and\n**(B)**\nby striking depicted and inserting identifiable ; and\n**(6)**\nby adding at the end the following:\n(6) Statute of limitations Any action commenced under this section shall be barred unless the complaint is filed not later than 10 years from the later of\u2014 (A) the date on which the identifiable individual reasonably discovers the violation that forms the basis for the claim; or (B) the date on which the identifiable individual reaches 18 years of age. (7) Duplicative recovery barred No relief may be ordered under paragraph (3) against a person who is subject to a judgment under section 2255 of title 18, United States Code, for the same conduct involving the same identifiable individual and the same intimate visual depiction or intimate digital forgery. .\n##### (c) Continued applicability of Federal, State, and Tribal law\n**(1) In general**\nThis Act shall not be construed to impair, supersede, or limit a provision of Federal, State, or Tribal law.\n**(2) No preemption**\nNothing in this Act shall prohibit a State or Tribal government from adopting and enforcing a provision of law governing disclosure of intimate images or nonconsensual activity involving an intimate digital forgery, as defined in section 1309(a) of the Consolidated Appropriations Act, 2022 ( 15 U.S.C. 6851(a) ), as amended by this Act, that is at least as protective of the rights of a victim as this Act.\n#### 4. Severability; rule of construction\n##### (a) Severability\nIf any provision of this Act, an amendment made by this Act, or the application of such a provision or amendment to any person or circumstance, is held to be unconstitutional, the remaining provisions of and amendments made by this Act, and the application of the provision or amendment held to be unconstitutional to any other person or circumstance, shall not be affected thereby.\n##### (b) Rule of construction\nNothing in this Act, or an amendment made by this Act, shall be construed to limit or expand any law pertaining to intellectual property.",
      "versionDate": "2025-05-21",
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
        "actionDate": "2026-01-13",
        "actionTime": "18:23:38",
        "text": "Held at the desk."
      },
      "number": "1837",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "DEFIANCE Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advanced technology and technological innovations",
            "updateDate": "2026-01-14T15:28:04Z"
          },
          {
            "name": "Assault and harassment offenses",
            "updateDate": "2026-01-14T15:28:04Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2026-01-14T15:28:04Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2026-01-14T15:28:04Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-01-14T15:28:04Z"
          },
          {
            "name": "Digital media",
            "updateDate": "2026-01-14T15:28:04Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2026-01-14T15:28:04Z"
          },
          {
            "name": "Photography and imaging",
            "updateDate": "2026-01-14T15:28:04Z"
          },
          {
            "name": "Pornography",
            "updateDate": "2026-01-14T15:28:04Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2026-01-14T15:28:04Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2026-01-14T15:28:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-29T15:59:51Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3562ih.xml"
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
      "title": "DEFIANCE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-29T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DEFIANCE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-29T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Disrupt Explicit Forged Images And Non-Consensual Edits Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-29T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve rights to relief for individuals affected by non-consensual activities involving intimate digital forgeries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-29T03:48:34Z"
    }
  ]
}
```
