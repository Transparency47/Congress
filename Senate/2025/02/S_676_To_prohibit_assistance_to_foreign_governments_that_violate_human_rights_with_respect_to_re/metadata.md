# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/676?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/676
- Title: Stop Funding Religiously Oppressive Regimes Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 676
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2025-05-07T16:22:22Z
- Update date including text: 2025-05-07T16:22:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/676",
    "number": "676",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "P000603",
        "district": "",
        "firstName": "Rand",
        "fullName": "Sen. Paul, Rand [R-KY]",
        "lastName": "Paul",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Stop Funding Religiously Oppressive Regimes Act of 2025",
    "type": "S",
    "updateDate": "2025-05-07T16:22:22Z",
    "updateDateIncludingText": "2025-05-07T16:22:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-20",
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
          "date": "2025-02-20T23:26:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s676is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 676\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Paul introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo prohibit assistance to foreign governments that violate human rights with respect to religious freedom.\n#### 1. Short title\nThis Act may be cited as the Stop Funding Religiously Oppressive Regimes Act of 2025 .\n#### 2. Identification of countries with laws imposing severe criminal penalties for apostasy, blasphemy, or interfaith\nNot later than 120 days after the date of the enactment of this Act, the President shall submit a report to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives that lists each foreign government that the President determines, based on credible information, imposes a death sentence or life imprisonment on the basis of\u2014\n**(1)**\nanti-apostasy laws that explicitly prohibit disaffiliation from a particular religion;\n**(2)**\nanti-blasphemy laws; or\n**(3)**\nlaws prohibiting marriage between individuals of different religious faiths.\n#### 3. Prohibition on assistance to foreign governments that violate human rights with respect to religion\nThe United States Government is prohibited from obligating or expending any Federal funds to provide assistance to the government of any country identified in the report submitted by the President pursuant to section 2.",
      "versionDate": "2025-02-20",
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
        "name": "International Affairs",
        "updateDate": "2025-05-07T16:22:22Z"
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
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s676is.xml"
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
      "title": "Stop Funding Religiously Oppressive Regimes Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T01:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Funding Religiously Oppressive Regimes Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit assistance to foreign governments that violate human rights with respect to religious freedom.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:43Z"
    }
  ]
}
```
