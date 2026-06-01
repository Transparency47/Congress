# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3609?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3609
- Title: Remove the Stain Act
- Congress: 119
- Bill type: HR
- Bill number: 3609
- Origin chamber: House
- Introduced date: 2025-05-23
- Update date: 2026-01-21T09:05:43Z
- Update date including text: 2026-01-21T09:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-23: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-05-23: Introduced in House

## Actions

- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-23",
    "latestAction": {
      "actionDate": "2025-05-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3609",
    "number": "3609",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "T000487",
        "district": "2",
        "firstName": "Jill",
        "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
        "lastName": "Tokuda",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Remove the Stain Act",
    "type": "HR",
    "updateDate": "2026-01-21T09:05:43Z",
    "updateDateIncludingText": "2026-01-21T09:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-23",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-23",
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
          "date": "2025-05-23T14:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "MN"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "KS"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "IL"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "NM"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "MN"
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
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "MI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MI"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3609ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3609\nIN THE HOUSE OF REPRESENTATIVES\nMay 23, 2025 Ms. Tokuda (for herself, Mr. Huffman , Ms. McCollum , Mr. Khanna , Ms. Davids of Kansas , Mr. Quigley , and Ms. Stansbury ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo rescind each Medal of Honor awarded for acts at Wounded Knee Creek on December 29, 1890, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Remove the Stain Act .\n#### 2. Findings\nCongress finds as follows:\n**(1)**\nThe Medal of Honor is the highest military award of the United States.\n**(2)**\nCongress found that to earn the Medal of Honor the deed of the person \u2026 must be so outstanding that it clearly distinguishes his gallantry beyond the call of duty from lesser forms of bravery .\n**(3)**\nThe actions of Medal of Honor recipients inspire bravery in those currently serving in the Armed Forces and those who will come to serve in the future.\n**(4)**\nThose listed on the Medal of Honor Roll have come to exemplify the best traits of members of the Armed Forces, a long and proud lineage of those who went beyond the call of service to the United States of America.\n**(5)**\nTo date the Medal of Honor has been awarded only 3,547 times, including only 151 times for the Korean War, 126 times in World War I, 28 times during the Global War on Terror, and 20 times for the massacre at Wounded Knee.\n**(6)**\nThe Medal of Honor is awarded in the name of Congress.\n**(7)**\nAs found in Senate Concurring Resolution 153 of the 101st Congress, on December 29, 1890, the 7th Cavalry of the United States engaged a tribal community resulting in the tragic death and injury of approximately 350\u2013375 Indian men, women, and children led by Lakota Chief Spotted Elk of the Miniconjou band at Cankpe' Opi Wakpa or Wounded Knee Creek .\n**(8)**\nThis engagement became known as the Wounded Knee Massacre , and took place between unarmed Native Americans and soldiers, heavily armed with standard issue army rifles as well as four Hotchkiss cannons capable of causing serious destruction.\n**(9)**\nNearly two-thirds of the Native Americans killed during the Massacre were unarmed women and children who were participating in a ceremony to restore their traditional homelands prior to the arrival of European settlers.\n**(10)**\nPoor tactical emplacement of the soldiers meant that most of the casualties suffered by the United States troops were inflicted by friendly fire.\n**(11)**\nOn January 1, 1891, Major General Nelson A. Miles, Commander of the Division of Missouri, telegraphed Major General John M. Schofield, Commanding General of the Army notifying him, It is stated that the disposition of four hundred soldiers and four pieces of artillery was fatally defective and large number of soldiers were killed and wounded by the fire from their own ranks and a very large number of women and children were killed in addition to the Indian men. .\n**(12)**\nThe United States awarded 20 Medals of Honor to soldiers of the U.S. 7th Cavalry following their participation in the Wounded Knee Massacre.\n**(13)**\nIn 2001, the Cheyenne River Sioux Tribe, a member Tribe of the Great Sioux Nation, upon information provided by Lakota elders and by veterans, passed Tribal Council Resolution No. 132\u201301, requesting that the Federal Government revoke the Medals of Honor from the soldiers of the United States Army, 7th Cavalry issued following the massacre of unarmed men, women, children, and elderly of the Great Sioux Nation on December 29, 1890, on Tribal Lands near Wounded Knee Creek.\n**(14)**\nThe National Congress of American Indians requested in a 2007 Resolution that the Congress renounce the issuance of said medals, and/or to proclaim that the medals are null and void, given the atrocities committed upon unarmed men, women, children and elderly of the Great Sioux Nation .\n**(15)**\nGeneral Miles contemporaneously stated that a wholesale massacre occurred and I have never heard of a more brutal, cold-blooded massacre than that at Wounded Knee .\n**(16)**\nAllowing any Medal of Honor, the United States highest and most prestigious military decoration, to recognize a member of the Armed Forces for distinguished service for participating in the massacre of hundreds of unarmed Native Americans is a disservice to the integrity of the United States and its citizens, and impinges on the integrity of the award and those who have earned the Medal since.\n#### 3. Rescission of Medals of Honor awarded for acts at Wounded Knee Creek on December 29, 1890\n##### (a) In general\nEach Medal of Honor awarded for acts at Wounded Knee Creek, Lakota Pine Ridge Indian Reservation, South Dakota, on December 29, 1890, is rescinded.\n##### (b) Medal of Honor Roll\nThe Secretary concerned shall remove the name of each individual awarded a Medal of Honor for acts described in subsection (a) from the Army, Navy, Air Force, and Coast Guard Medal of Honor Roll maintained under section 1134a of title 10, United States Code.\n##### (c) Return of medal not required\nNo person may be required to return to the Federal Government a Medal of Honor rescinded under subsection (a).\n##### (d) No denial of benefits\nThis Act shall not be construed to deny any individual any benefit from the Federal Government.",
      "versionDate": "2025-05-23",
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
        "actionDate": "2025-05-22",
        "text": "Read twice and referred to the Committee on Armed Services."
      },
      "number": "1915",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Remove the Stain Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-20T12:47:08Z"
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
      "date": "2025-05-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3609ih.xml"
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
      "title": "Remove the Stain Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Remove the Stain Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To rescind each Medal of Honor awarded for acts at Wounded Knee Creek on December 29, 1890, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:22Z"
    }
  ]
}
```
