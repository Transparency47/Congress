# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7511?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7511
- Title: Iowa National Guard Heroes Commemoration Act
- Congress: 119
- Bill type: HR
- Bill number: 7511
- Origin chamber: House
- Introduced date: 2026-02-11
- Update date: 2026-03-07T09:06:40Z
- Update date including text: 2026-03-07T09:06:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-11: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-02 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2026-02-11: Introduced in House

## Actions

- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-02 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7511",
    "number": "7511",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Iowa National Guard Heroes Commemoration Act",
    "type": "HR",
    "updateDate": "2026-03-07T09:06:40Z",
    "updateDateIncludingText": "2026-03-07T09:06:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-02",
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
      "actionDate": "2026-02-11",
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
      "actionDate": "2026-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T16:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-02T15:16:04Z",
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
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "IA"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "IA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7511ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7511\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2026 Mr. Nunn of Iowa (for himself, Mr. Feenstra , Mrs. Hinson , and Mrs. Miller-Meeks ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo designate the clinic of the Department of Veterans Affairs in Des Moines, Iowa, as the Staff Sergeant Edgar Torres-Tovar VA Clinic and to designate the community-based outpatient clinic of the Department in Marshalltown, Iowa, as the Staff Sergeant William Nathaniel Howard VA Clinic .\n#### 1. Short title\nThis Act may be cited as the Iowa National Guard Heroes Commemoration Act .\n#### 2. Designation of Staff Sergeant Edgar Torres-Tovar VA Clinic\n##### (a) Findings\nCongress finds the following:\n**(1)**\nStaff Sergeant Edgar Brian Torres-Tovar was born in DeKalb, Illinois, on October 17, 2000, and raised in Des Moines, Iowa.\n**(2)**\nStaff Sergeant Torres-Tovar graduated from Dowling Catholic High School in West Des Moines, Iowa, in 2019.\n**(3)**\nOn February 21, 2019, Staff Sergeant Torres-Tovar enlisted in the United States Army.\n**(4)**\nStaff Sergeant Torres-Tovar was the first in his family to serve in the Armed Forces.\n**(5)**\nStaff Sergeant Torres-Tovar deployed to Kosovo in November 2020, supporting United States and allied operations, and deployed to Syria in July 2025 in support of Operation Inherent Resolve.\n**(6)**\nStaff Sergeant Torres-Tovar served as a Cavalry Scout with Troop B, 1st Squadron, 113th Cavalry Regiment, 2nd Brigade Combat Team, 34th Infantry Division of the Iowa National Guard.\n**(7)**\nOn December 13, 2025, Staff Sergeant Torres-Tovar was killed in action in Palmyra, Syria, while supporting United States counterterrorism operations.\n**(8)**\nStaff Sergeant Torres-Tovar was awarded the Bronze Star Medal with Valor, the Purple Heart, the Combat Action Badge, and the Army Commendation Medal with Combat Device for heroic service during combat operations in support of Operation Inherent Resolve.\n##### (b) Designation\nThe clinic of the Department of Veterans Affairs located at 1211 East Army Post Road, Des Moines, Iowa, shall after the date of the enactment of this Act be known and designated as the Staff Sergeant Edgar Torres-Tovar VA Clinic or the Edgar Torres-Tovar VA Clinic .\n##### (c) References\nAny reference in any law, regulation, map, document, paper, or other record of the United States to the clinic referred to in subsection (b) shall be considered to be a reference to the Staff Sergeant Edgar Torres-Tovar VA Clinic.\n#### 3. Designation of Staff Sergeant William Nathaniel Howard VA Clinic\n##### (a) Findings\nCongress finds the following:\n**(1)**\nStaff Sergeant William Nathaniel Nate Howard was born on August 14, 1996, in Marshalltown, Iowa.\n**(2)**\nStaff Sergeant Howard graduated from Marshalltown High School in 2014.\n**(3)**\nAt the age of 17, while a high school senior, Staff Sergeant Howard enlisted in the Iowa National Guard on November 27, 2013, completing basic combat training and advanced individual training at Fort Benning, Georgia.\n**(4)**\nStaff Sergeant Howard deployed to Kosovo from November 2020 to July 2021 in support of United States and allied operations, served on the Texas border from April 2024 to May 2024, and deployed to Syria in July 2025 in support of Operation Inherent Resolve.\n**(5)**\nStaff Sergeant Howard served as a Cavalry Scout with Troop B, 1st Squadron, 113th Cavalry Regiment, 2nd Brigade Combat Team, 34th Infantry Division of the Iowa National Guard.\n**(6)**\nOn December 13, 2025, Staff Sergeant Howard was killed in action in Palmyra, Syria, while supporting United States counterterrorism operations.\n**(7)**\nStaff Sergeant Howard was awarded the Bronze Star Medal with Valor, the Purple Heart, the Combat Action Badge, and the Army Commendation Medal with Combat Device for heroic service in combat.\n##### (b) Designation\nThe outpatient clinic of the Department of Veterans Affairs located at 201 East Merle Hibbs Boulevard, Marshalltown, Iowa, shall after the date of the enactment of this Act be known and designated as the Staff Sergeant William Nathaniel Howard VA Clinic or the Nate Howard VA Clinic .\n##### (c) References\nAny reference in any law, regulation, map, document, paper, or other record of the United States to the clinic referred to in subsection (b) shall be considered to be a reference to the Staff Sergeant William Nathaniel Howard VA Clinic.",
      "versionDate": "2026-02-11",
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
        "actionDate": "2026-02-11",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "3837",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Iowa National Guard Heroes Commemoration Act",
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
        "updateDate": "2026-02-24T18:37:59Z"
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
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7511ih.xml"
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
      "title": "Iowa National Guard Heroes Commemoration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-23T13:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Iowa National Guard Heroes Commemoration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-23T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To designate the clinic of the Department of Veterans Affairs in Des Moines, Iowa, as the \"Staff Sergeant Edgar Torres-Tovar VA Clinic\" and to designate the community-based outpatient clinic of the Department in Marshalltown, Iowa, as the \"Staff Sergeant William Nathaniel Howard VA Clinic\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-23T13:18:36Z"
    }
  ]
}
```
