# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1435?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1435
- Title: Accountability in Foreign Animal Research Act
- Congress: 119
- Bill type: S
- Bill number: 1435
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2025-12-05T22:49:24Z
- Update date including text: 2025-12-05T22:49:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1435",
    "number": "1435",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Accountability in Foreign Animal Research Act",
    "type": "S",
    "updateDate": "2025-12-05T22:49:24Z",
    "updateDateIncludingText": "2025-12-05T22:49:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-04-10T17:42:54Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "MO"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1435is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1435\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Ms. Ernst (for herself and Mr. Schmitt ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo prohibit the use of taxpayer dollars to support animal experimentation in the laboratories of adversarial nations.\n#### 1. Short title\nThis Act may be cited as the Accountability in Foreign Animal Research Act .\n#### 2. Prohibition on funding research on animals in certain foreign countries\n##### (a) In general\nThe Secretary of Health and Human Services may not\u2014\n**(1)**\ndirectly or indirectly conduct biomedical research or experimentation that involves testing on vertebrate animals in any facility, or through any entity, located in, or owned or controlled, directly or indirectly, by\u2014\n**(A)**\nany of the foreign countries specified in subsection (b); or\n**(B)**\nsuch other foreign country that the Secretary of Health and Human Services, in consultation with the Secretary of State and the Secretary of Defense, determines is a foreign country of concern for the purposes of this Act; or\n**(2)**\nsupport, through grants, subgrants, contracts, cooperative agreements, or other funding vehicles, biomedical research or experimentation that involves testing on vertebrate animals conducted by any entity based in a foreign country referred to in paragraph (1).\n##### (b) Foreign countries specified\nThe foreign countries specified in this subsection are the following:\n**(1)**\nThe People\u2019s Republic of China, including the Hong Kong Special Administrative Region.\n**(2)**\nThe Islamic Republic of Iran.\n**(3)**\nThe Democratic People\u2019s Republic of Korea.\n**(4)**\nThe Russian Federation.\n##### (c) Report on addition to list of foreign countries\n**(1) In general**\nThe Secretary of Health and Human Services shall submit to the chairperson and ranking member of each of the appropriate committees of Congress a report with respect to each instance in which the Secretary makes a determination with respect to a country under subsection (a)(1)(B) that contains a detailed accounting of the Secretary\u2019s reasoning for such determination.\n**(2) Timing**\nA report shall be submitted under paragraph (1) not later than 60 days after the date of an instance described in such paragraph.\n**(3) Appropriate committees of Congress**\nIn this section, the term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Appropriations of the Senate;\n**(B)**\nthe Committee on Health, Education, Labor, and Pensions of the Senate;\n**(C)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate;\n**(D)**\nthe Committee on Appropriations of the House of Representatives;\n**(E)**\nthe Committee on Energy and Commerce of the House of Representatives; and\n**(F)**\nthe Committee on Homeland Security of the House of Representatives.",
      "versionDate": "2025-04-10",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-04-28",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "3043",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Accountability in Foreign Animal Research Act",
      "type": "HR"
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
        "name": "Health",
        "updateDate": "2025-05-23T14:12:24Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1435is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Accountability in Foreign Animal Research Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-12T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Accountability in Foreign Animal Research Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the use of taxpayer dollars to support animal experimentation in the laboratories of adversarial nations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:18:27Z"
    }
  ]
}
```
