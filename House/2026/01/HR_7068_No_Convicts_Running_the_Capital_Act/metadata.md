# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7068?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7068
- Title: No Convicts Running the Capital Act
- Congress: 119
- Bill type: HR
- Bill number: 7068
- Origin chamber: House
- Introduced date: 2026-01-14
- Update date: 2026-02-03T21:15:12Z
- Update date including text: 2026-02-03T21:15:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-01-14: Introduced in House

## Actions

- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7068",
    "number": "7068",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "No Convicts Running the Capital Act",
    "type": "HR",
    "updateDate": "2026-02-03T21:15:12Z",
    "updateDateIncludingText": "2026-02-03T21:15:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-14",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T15:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7068ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7068\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2026 Ms. Mace (for herself and Mr. Burchett ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit the District of Columbia government from appointing individuals convicted of crimes of violence or dangerous crimes as employees of the government or from entering into contracts with vendors who employ individuals convicted of crimes of violence or dangerous crimes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Convicts Running the Capital Act .\n#### 2. Prohibiting employment with district of columbia government of individuals convicted of violent crimes\n##### (a) Prohibition\nAn employing authority of an office of the District of Columbia government may not appoint an individual to a position in the District of Columbia government unless the individual certifies that the individual has not been finally convicted of a crime of violence or a dangerous crime.\n##### (b) Effective date; termination of current employees\n**(1) In general**\nSubsection (a) shall apply with respect to an individual appointed to a position in the District of Columbia government after the date of the enactment of this Act.\n**(2) Termination**\nNot later than 90 days after the date of the enactment of this Act, the District of Columbia shall terminate the employment of any individual who has been finally convicted of a crime of violence or a dangerous crime who holds a position in the District of Columbia government on the date of the enactment of this Act.\n#### 3. Prohibiting district of columbia government from entering into contracts with vendors employing individuals convicted of violent crimes\n##### (a) Prohibition\nAn office of the District of Columbia government may not enter into a contract with a vendor for the provision of goods or services unless the vendor certifies that the vendor is not a covered vendor.\n##### (b) Covered vendor defined\nIn this section, a vendor is a covered vendor with respect to a contract if either of the following applies:\n**(1)**\nIn the case of a vendor who is an individual, the vendor has been finally convicted of a crime of violence or a dangerous crime.\n**(2)**\nIn the case of a vendor who is an entity\u2014\n**(A)**\nthe vendor employs an individual who has been finally convicted of a crime of violence or a dangerous crime to provide goods or services under the contract;\n**(B)**\nan individual who has been finally convicted of a crime of violence or a dangerous crime serves as an officer or director of the vendor, including by serving on the vendor\u2019s board of directors; or\n**(C)**\nan individual who has been finally convicted of a crime of violence or a dangerous crime has a controlling ownership interest in the vendor.\n##### (c) Effective date; termination of current contracts\n**(1) In general**\nSubsection (a) shall apply with respect to contracts entered into after the date of the enactment of this Act.\n**(2) Termination**\nNot later than 90 days after the date of the enactment of this Act, the District of Columbia shall terminate any contract with a vendor who is a covered vendor which is in effect on the date of the enactment of this Act.\n#### 4. Definitions\nIn this Act, the following definitions apply:\n**(1)**\nThe term crime of violence has the meaning given such term in section 23\u20131331(4), District of Columbia Official Code, except that such term includes an offense under Federal, State, or local law which is substantially similar to an offense described in such section.\n**(2)**\nThe term dangerous crime has the meaning given such term in section 23\u20131331(3), District of Columbia Official Code, except that such term includes an offense under Federal, State, or local law which is substantially similar to an offense described in such section.\n**(3)**\nThe term finally convicted means a conviction\u2014\n**(A)**\nwhich has not been appealed and is no longer appealable because the time for taking an appeal has expired; or\n**(B)**\nwhich has been appealed and the appeals process for which is completed.",
      "versionDate": "2026-01-14",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-03T21:15:12Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7068ih.xml"
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
      "title": "No Convicts Running the Capital Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-28T08:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Convicts Running the Capital Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-28T08:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the District of Columbia government from appointing individuals convicted of crimes of violence or dangerous crimes as employees of the government or from entering into contracts with vendors who employ individuals convicted of crimes of violence or dangerous crimes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-28T08:33:20Z"
    }
  ]
}
```
