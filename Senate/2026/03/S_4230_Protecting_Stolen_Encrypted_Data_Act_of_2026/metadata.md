# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4230?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4230
- Title: Protecting Stolen Encrypted Data Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4230
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-15T01:25:01Z
- Update date including text: 2026-04-15T01:25:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Select Committee on Intelligence.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Select Committee on Intelligence.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4230",
    "number": "4230",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001076",
        "district": "",
        "firstName": "Maggie",
        "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
        "lastName": "Hassan",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Protecting Stolen Encrypted Data Act of 2026",
    "type": "S",
    "updateDate": "2026-04-15T01:25:01Z",
    "updateDateIncludingText": "2026-04-15T01:25:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Intelligence (Select) Committee",
          "systemCode": "slin00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Select Committee on Intelligence.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T17:42:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Intelligence (Select) Committee",
      "systemCode": "slin00",
      "type": "Select"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4230is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4230\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Ms. Hassan (for herself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Select Committee on Intelligence\nA BILL\nTo require the Federal Government to identify and address stolen sensitive data and classified information, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Stolen Encrypted Data Act of 2026 .\n#### 2. Addressing stolen sensitive data\n##### (a) Definitions\nIn this section:\n**(1) Classified information**\nThe term classified information has the meaning given such term in section 805 of the National Security Act of 1947 ( 50 U.S.C. 3164 ).\n**(2) Covered data**\nThe term covered data means includes the following:\n**(A)**\nFinancial, medical, and biometric data of United States persons.\n**(B)**\nIntellectual property of United States persons.\n**(C)**\nTrade secrets of United States persons.\n**(3) United States person**\nThe term United States person has the meaning given such term in section 101 of the Foreign Intelligence Surveillance Act of 1978 ( 50 U.S.C. 1801 ).\n##### (b) Addressing stolen sensitive data\n**(1) Strategies to identify**\nThe President shall, acting through the Secretary of Defense and the Director of National Intelligence, develop strategies to identify\u2014\n**(A)**\ncovered data and classified information unlawfully held by foreign entities;\n**(B)**\nwhether such data and information were encrypted; and\n**(C)**\nwhether such data and information have been decrypted by such foreign entities.\n**(2) Strategies to address**\nThe President shall, acting through the Secretary of Defense and the Director of National Intelligence, develop strategies regarding how to address stolen covered data and classified information.\n**(3) Destruction, manipulation, or recovery**\n**(A) Determination of economic and national security interest**\nThe Secretary and the Director shall jointly determine whether the destruction, manipulation, or recovery of covered data and classified information identified pursuant to the strategies developed under paragraph (1) would be in the economic and national security interest of the United States.\n**(B) Destruction, manipulation, or recovery**\nIn a case in which the Secretary and the Director jointly determine under subparagraph (A) that destroying, manipulating, or recovering covered data or classified information is in the economic and national security interested of the United States, the Secretary and the Director may jointly\u2014\n**(i)**\npursuant to strategies required by paragraph (1), identify encrypted covered data and classified information that is unlawfully held by a foreign entity that has not been decrypted by the foreign entity;\n**(ii)**\npursuant to the strategies required by paragraph (2), attempt to destroy, manipulate, or recover the data and information identified pursuant to clause (i); and\n**(iii)**\nwhen practicable, inform the lawful owners of covered data or classified information\u2014\n**(I)**\nof the intent of the Secretary or the Director, as the case may be, to destroy, manipulate, or recover the covered data or classified information; and\n**(II)**\nupon successful destruction, manipulation, or recovery of the covered data or classified information.\n##### (c) Report\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the Secretary and the Director shall jointly submit to Congress a report on the strategies developed under paragraphs (1) and (2) of subsection (c) and the actions taken under paragraph (3) of such subsection.\n**(2) Recommendations**\nThe report submitted pursuant to paragraph (1) shall include such recommendations as the Secretary and the Director may have for legislative or administrative action to carry out subsection (c).\n**(3) Form**\nThe report submitted pursuant to paragraph (1) shall be submitted in unclassified form, but may include a classified annex.",
      "versionDate": "2026-03-26",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-04-15T01:25:00Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4230is.xml"
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
      "title": "Protecting Stolen Encrypted Data Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-11T03:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Stolen Encrypted Data Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Federal Government to identify and address stolen sensitive data and classified information, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-11T03:48:22Z"
    }
  ]
}
```
