# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1437?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1437
- Title: Buffalo Soldiers Congressional Gold Medal Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1437
- Origin chamber: House
- Introduced date: 2025-02-18
- Update date: 2026-04-14T08:05:34Z
- Update date including text: 2026-04-14T08:05:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-18 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-18: Introduced in House

## Actions

- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-18 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1437",
    "number": "1437",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001159",
        "district": "10",
        "firstName": "Marilyn",
        "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
        "lastName": "Strickland",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Buffalo Soldiers Congressional Gold Medal Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-14T08:05:34Z",
    "updateDateIncludingText": "2026-04-14T08:05:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-18",
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
          "date": "2025-02-18T18:02:25Z",
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
          "date": "2025-02-18T18:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert [D-NJ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "NJ"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "AZ"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "WI"
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
      "sponsorshipDate": "2025-02-25",
      "state": "AL"
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
      "sponsorshipDate": "2025-02-25",
      "state": "DC"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "GA"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NJ"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "IN"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "KS"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
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
      "sponsorshipDate": "2025-03-04",
      "state": "CA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "MA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "FL"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "MT"
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
      "sponsorshipDate": "2025-03-10",
      "state": "NC"
    },
    {
      "bioguideId": "G000551",
      "district": "7",
      "firstName": "Ra\u00fal",
      "fullName": "Rep. Grijalva, Ra\u00fal M. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "AZ"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MD"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "IL"
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
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NM"
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
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NV"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "TX"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "AZ"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1437ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1437\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 18, 2025 Ms. Strickland (for herself and Mr. Conaway ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on House Administration , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo award a Congressional Gold Medal collectively to the Buffalo Soldier regiments, authorized by Congress in 1866 to serve in the United States Armed Forces, in recognition of their superior, dedicated, and vital service to our Nation.\n#### 1. Short title\nThis Act may be cited as the Buffalo Soldiers Congressional Gold Medal Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIn 1866, Congress passed the Army Organization Act which authorized the creation of six all-Black cavalry and infantry regiments. These regiments remained active until the Army was desegregated in 1951.\n**(2)**\nAccording to legend, American Indians called the Black cavalry troops Buffalo Soldiers because of their dark, curly hair, which resembled a buffalo\u2019s coat.\n**(3)**\nThe African-American troops accepted the name with pride and honor, as they were aware of the buffalo\u2019s fierce bravery and fighting spirit.\n**(4)**\nThe original six regiments melded into the following four regiments:\n**(A)**\nThe 9th Cavalry Regiment assembled in New Orleans, Louisiana, in August and September of 1866. They were ordered to San Antonio, Texas, in April 1867, with the mission to maintain order and to secure the road from San Antonio to El Paso.\n**(B)**\nThe 10th Cavalry Regiment gathered in Fort Leavenworth, Kansas, during the summer of 1867. In August 1867, they were ordered to Fort Riley, Kansas, with the mission of protecting the Pacific Railroad.\n**(C)**\nThe 24th Infantry Regiment was organized in 1869, forming from the 38th and 41st Colored Infantry Regiments. They served throughout the Western United States, with the mission to protect frontier posts and secure roadways.\n**(D)**\nThe 25th Infantry Regiment assembled at Camp William Penn, Pennsylvania, beginning in January 1864. They were assigned to numerous districts within the Department of the Gulf with the mission to maintain security.\n**(5)**\nBuffalo Soldiers also assisted in the protection of National Parks. They helped fight wildfires and poachers in the Yosemite and Sequoia National Parks and served as park rangers in the Sierra Nevada.\n**(6)**\nIn the Spanish-American War, all four regiments played key roles and fought with distinction, despite facing severe discrimination from the locals.\n**(7)**\nAt the start of World War I, the Buffalo Soldier regiments were dispatched to locations throughout the central United States and into the Pacific, offering logistics and support behind the front lines in the American Expeditionary Forces.\n**(8)**\nDuring World War II, African-American soldiers and units continued to serve proudly under the name Buffalo Soldier , including the 92nd Infantry Division, which was the only Black division that saw combat in Europe.\n**(9)**\nIn the Korean War, Buffalo Soldier regiments fought throughout the Korean peninsula, from the defense of the Pusan Perimeter to the counteroffensives which resulted in the end of armed hostilities and the creation of the Demilitarized Zone.\n**(10)**\nBuffalo Soldiers had the lowest military desertion and court-martial rates of their time. In recognition of combat valor and their actions beyond the call of duty, many were awarded the Congressional Medal of Honor.\n**(11)**\nThe Congressional Gold Medal would be an appropriate way to shed further light on the service of the Buffalo Soldiers and the instrumental role they played in instilling an approach to inclusivity within our military and the American way of life.\n#### 3. Congressional gold medal\n##### (a) Award authorized\nThe Speaker of the House of Representatives and the President pro tempore of the Senate shall make appropriate arrangements for the award, on behalf of Congress, of a single gold medal of appropriate design to the Buffalo Soldier regiments, authorized by Congress in 1866 to serve in the United States Armed Forces, in recognition of their superior, dedicated, and vital service to our Nation.\n##### (b) Design and striking\nFor the purposes of the award described in subsection (a), the Secretary of the Treasury (in this Act referred to as the Secretary ) shall strike a gold medal with suitable emblems, devices, and inscriptions, to be determined by the Secretary.\n##### (c) Smithsonian institution\n**(1) In general**\nFollowing the award of the gold medal under subsection (a), the gold medal shall be given to the National Museum of African American History and Culture of the Smithsonian Institution, where it shall be displayed as appropriate and made available for research.\n**(2) Sense of Congress**\nIt is the sense of Congress that the Smithsonian Institution should make the gold medal received under paragraph (1) available for display elsewhere, particularly at other locations and events associated with the Buffalo Soldiers.\n#### 4. Duplicate medals\nThe Secretary may strike and sell duplicates in bronze of the gold medal struck pursuant to section 3, at a price sufficient to cover the cost thereof, including labor, materials, dies, use of machinery, and overhead expenses.\n#### 5. Status of medals\n##### (a) National medals\nThe medals struck under this Act are national medals for purposes of chapter 51 of title 31, United States Code.\n##### (b) Numismatic items\nFor purposes of sections 5134 and 5136 of title 31, United States Code, all medals struck under this Act shall be considered to be numismatic items.\n#### 6. Authority to use fund amounts; proceeds of sale\n##### (a) Authority To use fund amounts\nThere is authorized to be charged against the United States Mint Public Enterprise Fund such amounts as may be necessary to pay for the costs of the medals struck under this Act.\n##### (b) Proceeds of sale\nAmounts received from the sale of duplicate bronze medals authorized under section 4 shall be deposited into the United States Mint Public Enterprise Fund.",
      "versionDate": "2025-02-18",
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
        "actionDate": "2025-07-28",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2487",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Buffalo Soldiers Congressional Gold Medal Act of 2025",
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
            "name": "Congressional tributes",
            "updateDate": "2025-07-09T14:38:52Z"
          },
          {
            "name": "Military history",
            "updateDate": "2025-07-09T14:38:52Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-07-09T14:38:52Z"
          },
          {
            "name": "Museums, exhibitions, cultural centers",
            "updateDate": "2025-07-09T14:38:52Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-07-09T14:38:52Z"
          },
          {
            "name": "Smithsonian Institution",
            "updateDate": "2025-07-09T14:38:52Z"
          },
          {
            "name": "Veterans' organizations and recognition",
            "updateDate": "2025-07-09T14:38:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-13T20:15:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-18",
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
          "measure-id": "id119hr1437",
          "measure-number": "1437",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-18",
          "originChamber": "HOUSE",
          "update-date": "2025-06-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1437v00",
            "update-date": "2025-06-09"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Buffalo Soldiers Congressional Gold Medal Act of 2025</strong></p><p>This bill provides for a Congressional Gold Medal to be awarded to the Buffalo Soldier regiments (six all-Black cavalry and infantry regiments authorized by Congress in 1866 to serve in the Armed Forces) in recognition of their vital service to the United States.</p>"
        },
        "title": "Buffalo Soldiers Congressional Gold Medal Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1437.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Buffalo Soldiers Congressional Gold Medal Act of 2025</strong></p><p>This bill provides for a Congressional Gold Medal to be awarded to the Buffalo Soldier regiments (six all-Black cavalry and infantry regiments authorized by Congress in 1866 to serve in the Armed Forces) in recognition of their vital service to the United States.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119hr1437"
    },
    "title": "Buffalo Soldiers Congressional Gold Medal Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Buffalo Soldiers Congressional Gold Medal Act of 2025</strong></p><p>This bill provides for a Congressional Gold Medal to be awarded to the Buffalo Soldier regiments (six all-Black cavalry and infantry regiments authorized by Congress in 1866 to serve in the Armed Forces) in recognition of their vital service to the United States.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119hr1437"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1437ih.xml"
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
      "title": "Buffalo Soldiers Congressional Gold Medal Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T09:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Buffalo Soldiers Congressional Gold Medal Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To award a Congressional Gold Medal collectively to the Buffalo Soldier regiments, authorized by Congress in 1866 to serve in the United States Armed Forces, in recognition of their superior, dedicated, and vital service to our Nation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T09:18:25Z"
    }
  ]
}
```
