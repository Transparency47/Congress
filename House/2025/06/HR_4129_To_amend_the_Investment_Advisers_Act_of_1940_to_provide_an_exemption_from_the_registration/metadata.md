# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4129?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4129
- Title: Tailoring for Main Street’s Investors Act
- Congress: 119
- Bill type: HR
- Bill number: 4129
- Origin chamber: House
- Introduced date: 2025-06-25
- Update date: 2025-12-10T09:06:01Z
- Update date including text: 2025-12-10T09:06:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-25: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-06-25: Introduced in House

## Actions

- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-25",
    "latestAction": {
      "actionDate": "2025-06-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4129",
    "number": "4129",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "G000597",
        "district": "2",
        "firstName": "Andrew",
        "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
        "lastName": "Garbarino",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Tailoring for Main Street\u2019s Investors Act",
    "type": "HR",
    "updateDate": "2025-12-10T09:06:01Z",
    "updateDateIncludingText": "2025-12-10T09:06:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-25",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-25",
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
          "date": "2025-06-25T14:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4129ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4129\nIN THE HOUSE OF REPRESENTATIVES\nJune 25, 2025 Mr. Garbarino introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Investment Advisers Act of 1940 to provide an exemption from the registration requirements under that Act to certain advisers of private funds, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tailoring for Main Street\u2019s Investors Act .\n#### 2. Exemption\nSection 203 of the Investment Advisers Act of 1940 ( 15 U.S.C. 80b\u20133 ) is amended by adding at the end the following:\n(o) Exemption from registration for certain private fund advisers (1) In general The Commission shall provide an exemption from the registration requirements under this section to any investment adviser of private funds, if\u2014 (A) the investment adviser acts solely as an investment adviser to private funds and has assets under management in the United States of less than $5,000,000,000; (B) each of the investors in each such private fund is\u2014 (i) a qualified purchaser, as defined in section 2(a) of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20132(a) ); (ii) an accredited investor, as defined in section 230.501(a) of title 17, Code of Federal Regulations, or any successor regulation; or (iii) an investment professional that is licensed by a national securities association registered pursuant to section 15A(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78o\u20133 ), if the Commission determines that the inclusion of such investment professionals would be appropriate; and (C) none of those private funds offers any investor of the private fund redemption or similar liquidity rights, except in extraordinary circumstances. (2) Reporting The Commission shall require investment advisers exempted by reason of this subsection to maintain such records and provide to the Commission every 2 years such reports as the Commission determines necessary or appropriate in the public interest or for the protection of investors, except that the requirements under this paragraph shall be no greater, and no more burdensome, than those under subsection (m)(2). .\n#### 3. Reporting for smaller advisers\n##### (a) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Securities and Exchange Commission.\n**(2) Covered entity**\nThe term covered entity means an entity that is required to submit Form ADV.\n**(3) Form ADV**\nThe term Form ADV means the form described in section 279.1 of title 17, Code of Federal Regulations, or any successor regulation.\n##### (b) Frequency of filing\nNotwithstanding any other provision of law or regulation, beginning on the date of enactment of this Act, a covered entity that has less than $1,000,000,000 in assets, as of the last day of the most recent fiscal year of the entity, shall be required to file Form ADV with the Commission not more frequently than once every 2 years.\n##### (c) Short form\nNot later than 280 days after the date of enactment of this Act, the Commission shall develop a short form version of Form ADV that a covered entity that has less than $1,000,000,000 in assets, as of the last day of the most recent fiscal year of the entity, may use to file Form ADV with the Commission.",
      "versionDate": "2025-06-25",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-07-16T13:14:41Z"
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
      "date": "2025-06-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4129ih.xml"
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
      "title": "Tailoring for Main Street\u2019s Investors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tailoring for Main Street\u2019s Investors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Investment Advisers Act of 1940 to provide an exemption from the registration requirements under that Act to certain advisers of private funds, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T05:18:32Z"
    }
  ]
}
```
