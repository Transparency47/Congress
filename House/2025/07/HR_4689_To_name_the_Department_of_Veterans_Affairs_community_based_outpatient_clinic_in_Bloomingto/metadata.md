# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4689?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4689
- Title: To name the Department of Veterans Affairs community-based outpatient clinic in Bloomington, Illinois, as the "Andrew Jackson Smith Medal of Honor Department of Veterans Affairs Clinic".
- Congress: 119
- Bill type: HR
- Bill number: 4689
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-03-31T14:56:27Z
- Update date including text: 2026-03-31T14:56:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4689",
    "number": "4689",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000585",
        "district": "16",
        "firstName": "Darin",
        "fullName": "Rep. LaHood, Darin [R-IL-16]",
        "lastName": "LaHood",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "To name the Department of Veterans Affairs community-based outpatient clinic in Bloomington, Illinois, as the \"Andrew Jackson Smith Medal of Honor Department of Veterans Affairs Clinic\".",
    "type": "HR",
    "updateDate": "2026-03-31T14:56:27Z",
    "updateDateIncludingText": "2026-03-31T14:56:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-19",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:11:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-19T19:07:26Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
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
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
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
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
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
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4689ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4689\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. LaHood (for himself, Mr. Jackson of Illinois , Ms. Kelly of Illinois , Mrs. Ramirez , Mr. Garc\u00eda of Illinois , Mr. Quigley , Mr. Casten , Mr. Davis of Illinois , Mr. Krishnamoorthi , Ms. Schakowsky , Mr. Schneider , Mr. Foster , Mr. Bost , Ms. Budzinski , Ms. Underwood , Mrs. Miller of Illinois , and Mr. Sorensen ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo name the Department of Veterans Affairs community-based outpatient clinic in Bloomington, Illinois, as the Andrew Jackson Smith Medal of Honor Department of Veterans Affairs Clinic .\n#### 1. Findings\nCongress makes the following findings:\n**(1)**\nColor Sergeant Andrew Jackson Smith of the 55th Massachusetts Infantry Regiment, formerly of the 41st Illinois Infantry Regiment, was posthumously awarded the Medal of Honor for his heroic actions in the Civil War.\n**(2)**\nHis Medal of Honor citation reads Corporal Andrew Jackson Smith, of Clinton, Illinois, a member of the 55th Massachusetts Voluntary Infantry, distinguished himself on 30 November 1864 by saving his regimental colors, after the color bearer was killed during a bloody charge at the Battle of Honey Hill, South Carolina. In the late afternoon, as the 55th Regiment pursued enemy skirmishers and conducted a running fight, they ran into a swampy area backed by a rise where the Confederate Army awaited. The surrounding woods and thick underbrush impeded infantry movement and artillery support. The 55th and 54th regiments formed columns to advance to the enemy position in a flanking movement. As the Confederates repelled other units, the 55th and 54th regiments continued to move into flanking positions. Forced into a narrow gorge crossing a swamp in the face of the enemy positions, the 55th's Color-Sergeant was killed by an exploding shell, and Corporal Smith took the Regimental Colors from his hand and carried them through heavy grape and canister fire. Although half of the officers and a third of the enlisted men engaged in the fight were killed or wounded, Corporal Smith continued to expose himself to the enemy fire by carrying the colors throughout the battle. Through his actions, the Regimental Colors of the 55th Infantry Regiment were not lost to the enemy. Corporal Andrew Jackson Smith's extraordinary valor in the face of deadly enemy fire is in keeping with the highest traditions of military service and reflect great credit upon him, the 55th Regiment, and the United States Army. .\n#### 2. Name of Department of Veterans Affairs community-based outpatient clinic, Bloomington, Illinois\nThe Department of Veterans Affairs community-based outpatient clinic located at 207 Hamilton Road, Bloomington, Illinois, shall after the date of enactment of this Act be known and designated as the Andrew Jackson Smith Medal of Honor Department of Veterans Affairs Clinic . Any reference to such clinic in any law, regulation, map, document, record, or other paper of the United States shall be considered to be a reference to the Andrew Jackson Smith Medal of Honor Department of Veterans Affairs Clinic.",
      "versionDate": "2025-07-23",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-19T17:29:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-23",
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
          "measure-id": "id119hr4689",
          "measure-number": "4689",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-23",
          "originChamber": "HOUSE",
          "update-date": "2026-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4689v00",
            "update-date": "2026-03-31"
          },
          "action-date": "2025-07-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill designates the community-based outpatient clinic of the Department of Veterans Affairs in Bloomington, Illinois, as the Andrew Jackson Smith Medal of Honor Department of Veterans Affairs Clinic.</p>"
        },
        "title": "To name the Department of Veterans Affairs community-based outpatient clinic in Bloomington, Illinois, as the \"Andrew Jackson Smith Medal of Honor Department of Veterans Affairs Clinic\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4689.xml",
    "summary": {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill designates the community-based outpatient clinic of the Department of Veterans Affairs in Bloomington, Illinois, as the Andrew Jackson Smith Medal of Honor Department of Veterans Affairs Clinic.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4689"
    },
    "title": "To name the Department of Veterans Affairs community-based outpatient clinic in Bloomington, Illinois, as the \"Andrew Jackson Smith Medal of Honor Department of Veterans Affairs Clinic\"."
  },
  "summaries": [
    {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill designates the community-based outpatient clinic of the Department of Veterans Affairs in Bloomington, Illinois, as the Andrew Jackson Smith Medal of Honor Department of Veterans Affairs Clinic.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4689"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4689ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To name the Department of Veterans Affairs community-based outpatient clinic in Bloomington, Illinois, as the \"Andrew Jackson Smith Medal of Honor Department of Veterans Affairs Clinic\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:48:33Z"
    },
    {
      "title": "To name the Department of Veterans Affairs community-based outpatient clinic in Bloomington, Illinois, as the \"Andrew Jackson Smith Medal of Honor Department of Veterans Affairs Clinic\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T08:05:59Z"
    }
  ]
}
```
