# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4918?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4918
- Title: Advancing Gun Safety Technology Act
- Congress: 119
- Bill type: HR
- Bill number: 4918
- Origin chamber: House
- Introduced date: 2025-08-08
- Update date: 2025-10-09T03:26:22Z
- Update date including text: 2025-10-09T03:26:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-08: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-08-08: Introduced in House

## Actions

- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-08",
    "latestAction": {
      "actionDate": "2025-08-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4918",
    "number": "4918",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "D000623",
        "district": "10",
        "firstName": "Mark",
        "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
        "lastName": "DeSaulnier",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Advancing Gun Safety Technology Act",
    "type": "HR",
    "updateDate": "2025-10-09T03:26:22Z",
    "updateDateIncludingText": "2025-10-09T03:26:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-08",
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
      "actionDate": "2025-08-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-08",
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
          "date": "2025-08-08T15:30:20Z",
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
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "CA"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "VA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4918ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4918\nIN THE HOUSE OF REPRESENTATIVES\nAugust 8, 2025 Mr. DeSaulnier (for himself, Ms. Lofgren , and Mr. Beyer ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo authorize the Attorney General to carry out a pilot program to make grants to entities to develop gun safety technology, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advancing Gun Safety Technology Act .\n#### 2. Gun safety technology pilot program\n##### (a) Authorization\nThe Attorney General, acting through the Director of the National Institute of Justice, is authorized to carry out a pilot program to make grants to eligible entities to develop gun safety technology.\n##### (b) Purpose\nThe purpose of the grant program under this section is to support the commercialization of technology that decreases the likelihood that a gun can be used accidentally or by unauthorized users.\n##### (c) Application\nAn eligible entity seeking a grant under this section shall submit to the Attorney General an application at such time, in such manner, and containing such information as the Attorney General may reasonably require, which information shall include a description of the entity's commitment and plans to develop gun safety technology and an initial gun safety product design.\n##### (d) Number of grants\nThe Attorney General shall make not less than 3 grants and not more than 5 grants under the pilot program under this section.\n##### (e) Report\nAn eligible entity receiving a grant under this section shall report to the Attorney General, at such times and including such information as the Attorney General may reasonably require, related milestones for the gun safety technology funded under this section, including the following:\n**(1)**\nBuilding a prototype.\n**(2)**\nConducting reliability testing.\n**(3)**\nPlanning for trial production.\n**(4)**\nPreparing to commercialize.\n##### (f) Authorization of appropriations\nThere is authorized to be appropriated $10,000,000 for fiscal year 2026.\n##### (g) Definitions\nIn this section:\n**(1)**\nThe term eligible entity means a small business concern (as defined under section 3 of the Small Business Act ( 15 U.S.C. 632 )) that has less than 500 employees.\n**(2)**\nThe term gun has the meaning given the term firearm in section 921 of title 18, United States Code.\n**(3)**\nThe term gun safety technology means technology that is designed to reduce the likelihood of an accidental or unauthorized use of a gun, including smart guns, user-authorized handguns, childproof guns, personalized guns, and safes and locking devices that include personalized technology.",
      "versionDate": "2025-08-08",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-18T19:52:43Z"
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
      "date": "2025-08-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4918ih.xml"
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
      "title": "Advancing Gun Safety Technology Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-12T03:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Advancing Gun Safety Technology Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Attorney General to carry out a pilot program to make grants to entities to develop gun safety technology, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T03:18:32Z"
    }
  ]
}
```
