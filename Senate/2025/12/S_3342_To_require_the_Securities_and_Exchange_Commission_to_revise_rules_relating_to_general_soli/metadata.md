# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3342?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3342
- Title: HALOS Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3342
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-02-04T05:06:15Z
- Update date including text: 2026-02-04T05:06:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3342",
    "number": "3342",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "HALOS Act of 2025",
    "type": "S",
    "updateDate": "2026-02-04T05:06:15Z",
    "updateDateIncludingText": "2026-02-04T05:06:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-S",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T15:29:29Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3342is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3342\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Mr. Ricketts (for himself and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require the Securities and Exchange Commission to revise rules relating to general solicitation or general advertising to allow for presentations or other communication made by or on behalf of an issuer at certain events, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Helping Angels Lead Our Startups Act of 2025 or the HALOS Act of 2025 .\n#### 2. Clarification of general solicitation\n##### (a) Definitions\nIn this section:\n**(1) Angel investor group**\nThe term angel investor group means any group that\u2014\n**(A)**\nis composed of accredited investors interested in investing personal capital in early-stage companies;\n**(B)**\nholds regular meetings and has defined processes and procedures for making investment decisions, either individually or among the membership of the group as a whole; and\n**(C)**\nis neither associated nor affiliated with brokers, dealers, or investment advisers.\n**(2) Issuer**\nThe term issuer means an issuer that is a business, is not in bankruptcy or receivership, is not an investment company, and is not a blank check, blind pool, or shell company.\n##### (b) Clarification\nNot later than 6 months after the date of enactment of this Act, the Securities and Exchange Commission shall revise sections 230.500 through 230.508 of title 17, Code of Federal Regulations (referred to in this subsection as Regulation D ), to require that, in carrying out the prohibition against general solicitation or general advertising contained in section 230.502(c) of that title, the prohibition shall not apply to a presentation or other communication made by or on behalf of an issuer that is made at an event\u2014\n**(1)**\nsponsored by\u2014\n**(A)**\nthe United States or any territory of the United States;\n**(B)**\nthe District of Columbia, any State, a federally recognized Indian Tribe; a political subdivision of any State, territory, or federally recognized Indian Tribe;\n**(C)**\nany agency or public instrumentality of any entity described in subparagraph (A) or (B);\n**(D)**\na college, university, or other institution of higher education;\n**(E)**\na nonprofit organization;\n**(F)**\nan angel investor group;\n**(G)**\nan incubator or accelerator;\n**(H)**\na venture forum, venture capital association, or trade association, other than an association created solely for the purpose of sponsoring an event described under this subsection; or\n**(I)**\nany other group, person, or entity as the Securities and Exchange Commission may determine by rule;\n**(2)**\nthat is not held in any facility that is owned or operated by a religious organization, other than an institution of higher education that is accredited and operated primarily for post-secondary education;\n**(3)**\nwhere any advertising for the event does not reference any specific offering of securities by the issuer;\n**(4)**\nthe sponsor of which\u2014\n**(A)**\ndoes not make investment recommendations or provide investment advice to event attendees;\n**(B)**\ndoes not engage in an active role in any investment negotiations between the issuer and investors attending the event;\n**(C)**\ndoes not charge event attendees any fees other than reasonable administrative fees;\n**(D)**\ndoes not receive any compensation for making introductions between investors attending the event and issuers, or for investment negotiations between such parties;\n**(E)**\nmakes readily available to attendees a disclosure not longer than one page in length, as prescribed by the Securities and Exchange Commission, describing the nature of the event and the risks of investing in the issuers presenting at the event; and\n**(F)**\ndoes not receive any compensation with respect to such event that would require registration of the sponsor as a broker or a dealer under the Securities Exchange Act of 1934 ( 15 U.S.C. 78a et seq. ), or as an investment advisor under the Investment Advisers Act of 1940 ( 15 U.S.C. 80b1 et seq. ); and\n**(5)**\nwhere no specific information regarding an offering of securities by the issuer is communicated or distributed by or on behalf of the issuer, other than\u2014\n**(A)**\nthat the issuer is in the process of offering securities or planning to offer securities;\n**(B)**\nthe type and amount of securities being offered;\n**(C)**\nthe amount of securities being offered that have already been subscribed for; and\n**(D)**\nthe intended use of proceeds of the offering.\n##### (c) Rule of construction\nSubsection (b) may only be construed as requiring the Securities and Exchange Commission to amend the requirements of Regulation D with respect to presentations and communications and not with respect to purchases or sales.\n##### (d) No pre-Existing substantive relationship by reason of event\nAttendance at an event described under subsection (b) shall not qualify, by itself, as establishing a pre-existing substantive relationship between an issuer and a purchaser for the purposes of section 230.506(b) of title 17, Code of Federal Regulations.",
      "versionDate": "2025-12-04",
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
        "actionDate": "2025-06-24",
        "text": "Received in the Senate and Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "3352",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "HALOS Act of 2025",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-01-07T17:18:19Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3342is.xml"
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
      "title": "HALOS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HALOS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Helping Angels Lead Our Startups Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Securities and Exchange Commission to revise rules relating to general solicitation or general advertising to allow for presentations or other communication made by or on behalf of an issuer at certain events, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-30T05:33:23Z"
    }
  ]
}
```
