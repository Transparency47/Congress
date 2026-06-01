# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/353?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/353
- Title: Commission to Relocate the Federal Bureaucracy Act
- Congress: 119
- Bill type: S
- Bill number: 353
- Origin chamber: Senate
- Introduced date: 2025-02-03
- Update date: 2025-06-20T18:47:08Z
- Update date including text: 2025-06-20T18:47:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-03: Introduced in Senate
- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-02-03: Introduced in Senate

## Actions

- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-03",
    "latestAction": {
      "actionDate": "2025-02-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/353",
    "number": "353",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Commission to Relocate the Federal Bureaucracy Act",
    "type": "S",
    "updateDate": "2025-06-20T18:47:08Z",
    "updateDateIncludingText": "2025-06-20T18:47:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-03",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-03",
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
          "date": "2025-02-03T20:37:52Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "LA"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "NC"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s353is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 353\nIN THE SENATE OF THE UNITED STATES\nFebruary 3, 2025 Mrs. Blackburn (for herself, Mr. Cassidy , Mr. Tillis , and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo establish a commission to study the relocation of certain agencies outside of the Washington, DC metropolitan area, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Commission to Relocate the Federal Bureaucracy Act .\n#### 2. Agency relocation commission\n##### (a) Definitions\n**(1) Agency**\nThe term agency has the meaning given the term in section 551 of title 5, United States Code.\n**(2) Commission**\nThe term Commission means the Commission established under subsection (b).\n**(3) Covered agency**\nThe term covered agency means an agency that is not a security-related agency, as determined by the President.\n**(4) Telework**\nThe term telework has the meaning given the term in section 6501 of title 5, United States Code.\n**(5) Washington, DC metropolitan area**\nThe term Washington, DC metropolitan area means\u2014\n**(A)**\nthe District of Columbia;\n**(B)**\nMontgomery and Prince George\u2019s Counties in the State of Maryland; and\n**(C)**\nArlington, Fairfax, Loudon, and Prince William Counties and the City of Alexandria in the Commonwealth of Virginia.\n##### (b) Establishment\nThere is established a Commission to study the relocation of covered agencies based in the Washington, DC metropolitan area to other areas throughout the United States.\n##### (c) Membership\nThe Commission shall be composed of\u2014\n**(1)**\nthe Director of the White House Presidential Personnel Office;\n**(2)**\nthe Director of the Office of Personnel Management;\n**(3)**\nthe Comptroller General of the United States;\n**(4)**\nthe Director of the Office of Management and Budget;\n**(5)**\nthe Secretary of Agriculture;\n**(6)**\nthe Secretary of Commerce;\n**(7)**\nthe Secretary of Education;\n**(8)**\nthe Secretary of Energy;\n**(9)**\nthe Secretary of Health and Human Services;\n**(10)**\nthe Secretary of Housing and Urban Development;\n**(11)**\nthe Secretary of the Interior;\n**(12)**\nthe Secretary of Labor;\n**(13)**\nthe Secretary of Transportation;\n**(14)**\nthe Secretary of Veterans Affairs;\n**(15)**\nthe Administrator of the Environmental Protection Agency; and\n**(16)**\nthe Commissioner of Food and Drugs.\n##### (d) Report\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Commission shall submit to Congress a report on the study described in subsection (b).\n**(2) Factors**\nIn developing the report required under paragraph (1), the Commission shall recommend the transfer of covered agencies with consideration of\u2014\n**(A)**\nfinancial efficiency, including whether the cost of living of an area is below the national average;\n**(B)**\nwhether an area has adequate pre-existing infrastructure and available private land to be used for the purpose of covered agencies;\n**(C)**\nwhether an area has existing industries relating to the business of a covered agency that can serve as public and private sector partners of the covered agency and strengthen the ability of the covered agency to carry out the duties of the covered agency;\n**(D)**\nwhether, at any time during the 5-year period preceding the date of enactment of this Act, not less than 50 percent of the workforce of the covered agency has participated in telework;\n**(E)**\nwhether an area maintains adequate technology infrastructure to allow agencies to operate efficiently; and\n**(F)**\nwhether an area is\u2014\n**(i)**\na qualified opportunity zone (as defined in section 1400Z\u20131(a) of the Internal Revenue Code of 1986); or\n**(ii)**\nan area that meets one or more of the criteria described in section 301(a) of the Public Works and Economic Development Act of 1965 ( 42 U.S.C. 3161(a) ).\n**(3) Community engagement**\nIn developing the report required under paragraph (1), the Commission shall consult with stakeholders that are local to potential relocation sites, including State and local government officials, business leaders from relevant industries, representatives from regional economic development agencies, and residents.\n**(4) Relocation target**\nIn developing the report required under paragraph (1), the Commission shall prioritize achieving a goal of transferring not fewer than 100,000 employees of covered agencies outside of the Washington, DC metropolitan area.",
      "versionDate": "2025-02-03",
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
        "actionDate": "2025-01-03",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "202",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Commission to Relocate the Federal Bureaucracy Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advisory bodies",
            "updateDate": "2025-06-20T18:46:44Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-20T18:47:04Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-06-20T18:46:59Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-06-20T18:46:52Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-06-20T18:47:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-14T15:12:44Z"
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
      "date": "2025-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s353is.xml"
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
      "title": "Commission to Relocate the Federal Bureaucracy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-14T03:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Commission to Relocate the Federal Bureaucracy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T03:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a commission to study the relocation of certain agencies outside of the Washington, DC metropolitan area, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T03:33:38Z"
    }
  ]
}
```
