# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3081?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3081
- Title: Law Enforcement Solidarity Act
- Congress: 119
- Bill type: HR
- Bill number: 3081
- Origin chamber: House
- Introduced date: 2025-04-29
- Update date: 2025-11-20T09:06:42Z
- Update date including text: 2025-11-20T09:06:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-29: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-29: Introduced in House

## Actions

- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-29",
    "latestAction": {
      "actionDate": "2025-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3081",
    "number": "3081",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Law Enforcement Solidarity Act",
    "type": "HR",
    "updateDate": "2025-11-20T09:06:42Z",
    "updateDateIncludingText": "2025-11-20T09:06:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-29",
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
      "actionDate": "2025-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-29",
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
          "date": "2025-04-29T14:01:05Z",
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
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "IL"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3081ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3081\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2025 Ms. Tenney introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide that jurisdictions with law enforcement cooperation restrictions are ineligible for certain Federal funds, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Law Enforcement Solidarity Act .\n#### 2. Jurisdictions with law enforcement cooperation restrictions ineligible for certain Federal funds\nBeginning in the first fiscal year that begins after the date that is 60 days after the date of enactment of this Act, for a fiscal year during which the Attorney General determines that a jurisdiction is a jurisdiction with law enforcement cooperation restrictions, such jurisdiction is ineligible to receive any Federal funds that such jurisdiction intends to use for the benefit (including the provision of food, shelter, healthcare services, legal services, and transportation) of aliens who are present in the United States without lawful status under the immigration laws.\n#### 3. Report on jurisdiction with law enforcement cooperation restrictions\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Attorney General shall submit to the Committee on the Judiciary of the House of Representatives and the Committee on the Judiciary of the Senate a report that includes a list of each jurisdiction that the Attorney General determines is a jurisdiction with law enforcement cooperation restrictions.\n#### 4. Definitions\nFor purposes of this Act:\n**(1)**\nthe term jurisdiction with law enforcement cooperation restrictions means any State or political subdivision of a State that has in effect a statute, ordinance, policy, or practice that prohibits or restricts any government entity or official from assisting, aiding, cooperating with, providing back-up to, or responding to a call made by a Federal law enforcement officer.\n**(2)**\nThe terms alien and immigration laws have the meanings given such term in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n**(3)**\nThe term Federal law enforcement officer has the meaning given such term in section 115(c)(1) of title 18, United States Code, and includes such an officer employed by the Department of Homeland Security.",
      "versionDate": "2025-04-29",
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
        "updateDate": "2025-05-21T12:40:23Z"
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
      "date": "2025-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3081ih.xml"
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
      "title": "Law Enforcement Solidarity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T05:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Law Enforcement Solidarity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide that jurisdictions with law enforcement cooperation restrictions are ineligible for certain Federal funds, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:34Z"
    }
  ]
}
```
