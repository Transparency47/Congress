# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4098?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4098
- Title: Stopping Proxy Advisor Racketeering Act
- Congress: 119
- Bill type: HR
- Bill number: 4098
- Origin chamber: House
- Introduced date: 2025-06-24
- Update date: 2025-07-17T10:37:44Z
- Update date including text: 2025-07-17T10:37:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-24: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-06-24: Introduced in House

## Actions

- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4098",
    "number": "4098",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "F000471",
        "district": "5",
        "firstName": "Scott",
        "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
        "lastName": "Fitzgerald",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Stopping Proxy Advisor Racketeering Act",
    "type": "HR",
    "updateDate": "2025-07-17T10:37:44Z",
    "updateDateIncludingText": "2025-07-17T10:37:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-24",
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
      "actionDate": "2025-06-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-24",
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
          "date": "2025-06-24T14:02:40Z",
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
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4098ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4098\nIN THE HOUSE OF REPRESENTATIVES\nJune 24, 2025 Mr. Fitzgerald introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Securities Exchange Act of 1934 to prohibit certain acts by proxy advisory firms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stopping Proxy Advisor Racketeering Act .\n#### 2. Conduct of proxy advisory firms\nThe Securities Exchange Act of 1934 ( 15 U.S.C. 78a et seq. ) is amended by inserting after section 14B the following:\n14C. Conduct of proxy advisory firms (a) Prohibited conduct It shall be unlawful for a proxy advisory firm to provide proxy voting advice if the proxy advisory firm possesses a conflict of interest, direct or indirect, including by\u2014 (1) providing consulting services offered directly or indirectly through an affiliate to a registrant; (2) modifying a voting recommendation or otherwise departing from the adopted systematic procedures and methodologies of the proxy advisory firm or affiliate for the provision of proxy voting advice based on whether a registrant, or affiliate of the registrant, subscribes or will subscribe to the services or products of the proxy advisory firm or any affiliate of the proxy advisory firm; (3) providing proxy voting advice during any period of time when the proxy advisory firm or any affiliate of the proxy advisory firm is providing stewardship or engagement services to a shareholder proponent, a non-issuer, a soliciting person, or affiliate of any of the foregoing related to the matter covered by the proxy voting advice; or (4) being a member of any organization that supports a shareholder-sponsored proposal that is, or is substantially the same subject matters as, the proxy voting advice. (b) Administrative civil penalties available If the Commission finds, after notice and opportunity for hearing in a proceeding instituted pursuant to section 21C, that a proxy advisory firm violated subsection (a), the Commission may, in addition to entering an order under section 21C, impose a civil penalty against the proxy advisory firm and any other person that the Commission finds was a cause of such violation. The determination to impose such a civil penalty and the amount of the penalty shall be governed by the standards set forth in section 21B. (c) Definitions In this section: (1) Consulting services With respect to a proxy advisory firm or an affiliate of a proxy advisory firm, the term consulting services means\u2014 (A) providing any non-public information with respect to a proxy advisory firm\u2019s polices or ratings methodologies; (B) any services designed to provide guidance or advice regarding any corporate governance, compensation, corporate social responsibility, environmental, social, political, or other policies, disclosures, or actions adopted by a registrant with respect to\u2014 (i) any matter\u2014 (I) for which security holder vote or consent is or will be solicited; and (II) as to which the proxy advisory firm makes or will make a recommendation as to a security holder\u2019s vote or consent; or (ii) matters included in or covered by any written report or rating furnished by the proxy advisory firm; and (C) such other services as the Commission may determine. (2) Proxy advisory firm The term proxy advisory firm means a person that markets the person\u2019s expertise as a provider of proxy voting advice, separately from other forms of investment advice, and sells such proxy voting advice for a fee. (3) Proxy voting advice The term proxy voting advice means any advice that makes a recommendation to a security holder as to the vote, consent, or authorization of the security holder on a specific matter for which the approval of the security holder is solicited. (4) Registrant The term registrant means the issuer of the securities in respect of which proxies are to be solicited. .",
      "versionDate": "2025-06-24",
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
        "updateDate": "2025-07-17T10:37:44Z"
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
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4098ih.xml"
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
      "title": "Stopping Proxy Advisor Racketeering Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-10T13:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stopping Proxy Advisor Racketeering Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-10T13:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Securities Exchange Act of 1934 to prohibit certain acts by proxy advisory firms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-10T13:48:20Z"
    }
  ]
}
```
