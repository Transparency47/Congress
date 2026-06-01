# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7780?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7780
- Title: One Nation, One Visa Policy Act
- Congress: 119
- Bill type: HR
- Bill number: 7780
- Origin chamber: House
- Introduced date: 2026-03-03
- Update date: 2026-04-17T08:07:27Z
- Update date including text: 2026-04-17T08:07:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-03-03: Introduced in House

## Actions

- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7780",
    "number": "7780",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "T000165",
        "district": "7",
        "firstName": "Thomas",
        "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
        "lastName": "Tiffany",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "One Nation, One Visa Policy Act",
    "type": "HR",
    "updateDate": "2026-04-17T08:07:27Z",
    "updateDateIncludingText": "2026-04-17T08:07:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
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
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T17:02:25Z",
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
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "TX"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7780ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7780\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2026 Mr. Tiffany (for himself and Mr. Roy ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit the Secretary of Homeland Security from admitting to the United States any national of the People\u2019s Republic of China without a valid visa, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the One Nation, One Visa Policy Act .\n#### 2. Prohibition on visa-free admission of Chinese nationals\n##### (a) In general\nThe Secretary of Homeland Security shall not admit any national of the People's Republic of China, or any individual bearing a passport issued by the People's Republic of China, who is not in possession of a valid visa.\n##### (b) Prohibition on use of funds\nNo funds appropriated or otherwise made available to the Department of Homeland Security may be used to allow the participation of any national of the People's Republic of China in the Guam and Commonwealth of the Northern Mariana Islands Visa Waiver Program authorized by section 212(l) of the Immigration and Nationality Act ( 8 U.S.C. 1182(l) ), including the Economic Vitality & Security Travel Authorization Program, or any other program that authorizes the admission of nationals of the People's Republic of China without a valid visa.\n##### (c) Definitions\nIn this section:\n**(1) In general**\nExcept as otherwise explicitly provided, a term used in this section shall have the meaning given such term in the immigration laws.\n**(2) Immigration laws**\nThe term immigration laws has the meaning given the term in section 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) ).\n**(3) People's Republic of China**\nThe term People's Republic of China includes the Special Administrative Unit of Hong Kong and the Special Administrative Unit of Macau.",
      "versionDate": "2026-03-03",
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
        "actionDate": "2026-02-12",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3857",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "One Nation, One Visa Policy Act",
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
        "updateDate": "2026-03-26T19:11:02Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7780ih.xml"
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
      "title": "One Nation, One Visa Policy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T07:23:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "One Nation, One Visa Policy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T07:23:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Secretary of Homeland Security from admitting to the United States any national of the People's Republic of China without a valid visa, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T07:18:22Z"
    }
  ]
}
```
