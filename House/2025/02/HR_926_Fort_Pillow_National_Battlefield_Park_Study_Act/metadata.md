# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/926?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/926
- Title: Fort Pillow National Battlefield Park Study Act
- Congress: 119
- Bill type: HR
- Bill number: 926
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2026-01-15T09:06:58Z
- Update date including text: 2026-01-15T09:06:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-01-07 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-01-14 - Committee: Subcommittee Hearings Held
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-01-07 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-01-14 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/926",
    "number": "926",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C001068",
        "district": "9",
        "firstName": "Steve",
        "fullName": "Rep. Cohen, Steve [D-TN-9]",
        "lastName": "Cohen",
        "party": "D",
        "state": "TN"
      }
    ],
    "title": "Fort Pillow National Battlefield Park Study Act",
    "type": "HR",
    "updateDate": "2026-01-15T09:06:58Z",
    "updateDateIncludingText": "2026-01-15T09:06:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-14",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-07",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Federal Lands.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
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
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:09:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-01-14T19:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-01-07T18:17:06Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
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
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "RI"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "IN"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "LA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "IL"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "IL"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "IL"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "DC"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MD"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MS"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "GA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr926ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 926\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Cohen (for himself, Mr. Amo , Mr. Carson , Mr. Carter of Louisiana , Mr. Davis of Illinois , Mr. Doggett , Mr. Green of Texas , Mr. Jackson of Illinois , Ms. Kelly of Illinois , Mrs. McIver , Ms. Norton , Mr. Raskin , and Mr. Thompson of Mississippi ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo conduct a special resource study of Fort Pillow Historic State Park in Henning, Tennessee, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Fort Pillow National Battlefield Park Study Act .\n#### 2. Findings\nCongress finds as follows:\n**(1)**\nFort Pillow was originally built by Confederate troops in 1861 and named after General Gideon J. Pillow of Maury County, Tennessee.\n**(2)**\nThe battle of Fort Pillow was fought on April 12, 1864, at Fort Pillow in Henning, Tennessee, during the American Civil War.\n**(3)**\nAt Fort Pillow, Tennessee, Confederate forces never defeated the Union Navy. Instead, they perpetrated a heinous massacre after violating a flag of truce by advantageously repositioning rebel troops and by looting government buildings and private storefronts surrounding the fort.\n**(4)**\nAccording to the 1864 Report Fort Pillow Massacre from the United States Congress Joint Committee on the Conduct of the War, The officers and men seem to vie with each other in the devilish work; men, women and even children, wherever found, were deliberately shot down, beaten and hacked with sabers. \u2026 .\n**(5)**\nThe Union garrison consisted of 19 officers and 538 troops of whom 262 were United States Colored Troops (U.S.C.T.).\n**(6)**\nPer the report, Of the men, from three hundred to four hundred are known to have been killed at Fort Pillow, of whom at least three hundred were murdered in cold blood after the fort was in possession of the rebels and our men had thrown down their arms and ceased to offer resistance. .\n**(7)**\nThe massacre at Fort Pillow demonstrated to all U.S.C.T. that surrender was not an option. The massacre at Fort Pillow became a rallying cry and motivation for the 209,147 U.S.C.T.\n**(8)**\nThe 209,147 U.S.C.T. fundamentally contributed to the Union\u2019s defeat of the Confederacy.\n**(9)**\nIn 1971, Fort Pillow became a State park.\n**(10)**\nIn 1973, Fort Pillow was added to the National Register of Historic Places.\n**(11)**\nThe following year, in 1974, Fort Pillow was designated as a National Historic Landmark.\n**(12)**\nFort Pillow Historic State Park consists of 1,642 acres.\n**(13)**\nThe Park contains several attraction areas such as a Civil War museum, hiking trail, camping ground, and picnic area.\n**(14)**\nThis site deserves to become a National Battlefield Park due to its profound effect on U.S.C.T. and all Union forces in their fight to preserve the United States of America.\n#### 3. Fort Pillow Special Resource Study\nThe Secretary of the Interior shall conduct a special resource study of Fort Pillow Historic State Park in Henning, Tennessee. Fort Pillow is a State park that features the American Civil War history and the Massacre at Fort Pillow. The Secretary shall\u2014\n**(1)**\nevaluate the site's national significance; and\n**(2)**\ndetermine the suitability and feasibility of designating it as a unit of the National Historic Park System.",
      "versionDate": "2025-02-04",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Conflicts and wars",
            "updateDate": "2025-06-18T14:00:11Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-06-18T14:00:11Z"
          },
          {
            "name": "Historic sites and heritage areas",
            "updateDate": "2025-06-18T14:00:11Z"
          },
          {
            "name": "Military history",
            "updateDate": "2025-06-18T14:00:11Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-06-18T14:00:11Z"
          },
          {
            "name": "Tennessee",
            "updateDate": "2025-06-18T14:00:11Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2025-06-18T14:00:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-01T20:23:12Z"
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
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr926ih.xml"
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
      "title": "Fort Pillow National Battlefield Park Study Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:50Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fort Pillow National Battlefield Park Study Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To conduct a special resource study of Fort Pillow Historic State Park in Henning, Tennessee, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:56Z"
    }
  ]
}
```
