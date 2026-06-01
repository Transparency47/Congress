# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5643?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5643
- Title: To name the Department of Veterans Affairs medical center located in Northport, New York, as the Navy (SEAL) Lieutenant Michael P. Murphy VA Medical Center, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 5643
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2026-04-16T08:06:50Z
- Update date including text: 2026-04-16T08:06:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5643",
    "number": "5643",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000598",
        "district": "1",
        "firstName": "Nick",
        "fullName": "Rep. LaLota, Nick [R-NY-1]",
        "lastName": "LaLota",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "To name the Department of Veterans Affairs medical center located in Northport, New York, as the Navy (SEAL) Lieutenant Michael P. Murphy VA Medical Center, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-04-16T08:06:50Z",
    "updateDateIncludingText": "2026-04-16T08:06:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
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
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
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
      "bioguideId": "L000603",
      "district": "8",
      "firstName": "Morgan",
      "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Luttrell",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "TX"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "VA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "False",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
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
      "sponsorshipDate": "2025-10-10",
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
      "sponsorshipDate": "2025-10-21",
      "state": "NY"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NY"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5643ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5643\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mr. LaLota (for himself, Mr. Luttrell , Mr. Lawler , Ms. Tenney , Ms. Malliotakis , Mr. Suozzi , and Mr. McGuire ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo name the Department of Veterans Affairs medical center located in Northport, New York, as the Navy (SEAL) Lieutenant Michael P. Murphy VA Medical Center, and for other purposes.\n#### 1. Findings\nCongress finds the following:\n**(1)**\nMichael Patrick Murphy was born on May 7, 1976, in Smithtown, New York, and grew up in Patchogue, New York, on Long Island.\n**(2)**\nMurphy graduated from Patchogue-Medford High School in 1994 and later attended Penn State University, earning dual degrees in political science and psychology.\n**(3)**\nOn June 28, 2005, Lieutenant Murphy was the officer-in-charge of a four-man SEAL element in support of Operation Red Wings. Shortly after arriving at the objective area, the SEALs were spotted by three anti-coalition militia sympathizers, who revealed their position to Taliban fighters.\n**(4)**\nLieutenant Murphy\u2019s team found themselves in a fierce gun battle against a much larger enemy force on the steep face of a mountain. Ignoring his own wounds and demonstrating exceptional composure, Lieutenant Murphy continued to lead his men in engaging the enemy. In the face of almost certain death, he fought his way into open terrain to gain a better position to transmit a call for assistance.\n**(5)**\nThis deliberate, heroic act exposed him to direct enemy fire. Finally achieving contact with his headquarters, Lieutenant Murphy maintained his exposed position while he provided his location and requested immediate support. In his final act of bravery, he continued to engage the enemy until he was mortally wounded, gallantly giving his life for his country and for the cause of freedom.\n**(6)**\nEight additional Navy SEALs and eight members of the U.S. Army\u2019s 160th Special Operations Aviation Regiment, the Night Stalkers , were also killed in the ensuing rescue when their MH\u201347 Chinook helicopter was struck by a rocket-propelled grenade.\n**(7)**\nLieutenant Murphy was posthumously awarded the Medal of Honor, our nation\u2019s highest military honor, for his heroic actions above and beyond the call of duty at the risk of his own life, the first Medal of Honor awarded for combat in Afghanistan, and the first for the Navy since the Vietnam War.\n**(8)**\nLieutenant Murphy\u2019s selfless leadership and courage continue to inspire many throughout this country and the world. Every year, people around the world complete the Murph workout in his honor. The LT Michael P. Murphy Memorial Scholarship Foundation now awards over 43 scholarships annually to further his belief that education will set you free , and the LT Michael P. Murphy Navy SEAL Museum in West Sayville, New York, hosts training and education for the local Sea Cadet division to develop character and confidence in the youth of Long Island who hope to follow in his footsteps.\n**(9)**\nNaming the Veterans Affairs Medical Center in Northport, New York, after LT Michael P. Murphy, only roughly ten miles from his birthplace, will serve as an enduring reminder of his selfless sacrifice, and help to educate future generations on the value of service, the cost of freedom, and the legacy of all who have given that last full measure in defense of this great nation.\n#### 2. Name of Department of Veterans Affairs medical center, Northport, New York\nThe Department of Veterans Affairs medical center located in Northport, New York, shall, after the date of the enactment of this Act, be known and designated as the Navy (SEAL) Lieutenant Michael P. Murphy VA Medical Center . Any reference to such medical center in any law, regulation, map, document, record, or other paper of the United States shall be considered to be a reference to the Navy (SEAL) Lieutenant Michael P. Murphy VA Medical Center.",
      "versionDate": "2025-09-30",
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
        "updateDate": "2025-11-19T19:59:32Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5643ih.xml"
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
      "title": "To name the Department of Veterans Affairs medical center located in Northport, New York, as the Navy (SEAL) Lieutenant Michael P. Murphy VA Medical Center, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T02:48:14Z"
    },
    {
      "title": "To name the Department of Veterans Affairs medical center located in Northport, New York, as the Navy (SEAL) Lieutenant Michael P. Murphy VA Medical Center, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T08:06:19Z"
    }
  ]
}
```
