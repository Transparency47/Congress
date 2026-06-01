# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/245?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/245
- Title: A resolution condemning the financial entanglements of President Donald J. Trump with the $TRUMP meme coin.
- Congress: 119
- Bill type: SRES
- Bill number: 245
- Origin chamber: Senate
- Introduced date: 2025-05-21
- Update date: 2025-06-25T23:09:14Z
- Update date including text: 2025-06-25T23:09:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in Senate
- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S3066)
- Latest action: 2025-05-21: Introduced in Senate

## Actions

- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S3066)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/245",
    "number": "245",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "A resolution condemning the financial entanglements of President Donald J. Trump with the $TRUMP meme coin.",
    "type": "SRES",
    "updateDate": "2025-06-25T23:09:14Z",
    "updateDateIncludingText": "2025-06-25T23:09:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S3066)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T23:53:18Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres245is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 245\nIN THE SENATE OF THE UNITED STATES\nMay 21, 2025 Mr. Blumenthal submitted the following resolution; which was referred to the Committee on Homeland Security and Governmental Affairs\nRESOLUTION\nCondemning the financial entanglements of President Donald J. Trump with the $TRUMP meme coin.\nThat the Senate\u2014\n**(1)**\ncondemns the financial entanglements of President Donald J. Trump with the $TRUMP meme coin for\u2014\n**(A)**\npermitting and facilitating covert payments to the President and the Trump family, including potential investments from foreign governments and foreign nationals under Federal prosecution; and\n**(B)**\nauctioning access to the Presidency in return for the purchase of the cryptocurrency of President Trump;\n**(2)**\naffirms that any purchase of $TRUMP by a foreign government is a violation of the Foreign Emoluments Clause of the Constitution of the United States because President Donald J. Trump did not seek the consent of Congress before accepting such payments; and\n**(3)**\ndemands the transfer of any proceeds from any foreign government purchase of $TRUMP nevertheless received by President Donald J. Trump in violation of the Foreign Emoluments Clause contained in clause 8 of section 9 of article I of the Constitution of the United States to the United States Government.",
      "versionDate": "2025-05-21",
      "versionType": "IS"
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-28T12:53:42Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres245is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution condemning the financial entanglements of President Donald J. Trump with the $TRUMP meme coin.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-24T03:33:43Z"
    },
    {
      "title": "A resolution condemning the financial entanglements of President Donald J. Trump with the $TRUMP meme coin.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-23T10:56:33Z"
    }
  ]
}
```
