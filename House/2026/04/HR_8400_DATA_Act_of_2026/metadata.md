# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8400?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8400
- Title: DATA Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8400
- Origin chamber: House
- Introduced date: 2026-04-21
- Update date: 2026-05-04T14:09:21Z
- Update date including text: 2026-05-04T14:09:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-21: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-04-21: Introduced in House

## Actions

- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-21",
    "latestAction": {
      "actionDate": "2026-04-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8400",
    "number": "8400",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "B001323",
        "district": "",
        "firstName": "Nicholas",
        "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
        "lastName": "Begich",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "DATA Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-04T14:09:21Z",
    "updateDateIncludingText": "2026-05-04T14:09:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-21",
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
          "date": "2026-04-21T14:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "TX"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8400ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8400\nIN THE HOUSE OF REPRESENTATIVES\nApril 21, 2026 Mr. Begich (for himself, Mr. Crenshaw , and Mr. Owens ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Power Act to exempt consumer-regulated electric utilities from Federal regulation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Decentralized Access to Technology Alternatives Act of 2026 or the DATA Act of 2026 .\n#### 2. Definitions\nIn this Act:\n**(1) Bulk-power system**\nThe term bulk-power system has the meaning given the term in section 215(a) of the Federal Power Act ( 16 U.S.C. 824o(a) ).\n**(2) Consumer-regulated electric utility; CREU**\nThe term consumer-regulated electric utility or CREU means an electric generation and supply system that\u2014\n**(A)**\nis established\u2014\n**(i)**\nafter the date of enactment of this Act; and\n**(ii)**\nexclusively for the purpose of serving new electric loads that were not previously served by any retail electricity supplier;\n**(B)**\nmay own, construct, and operate facilities necessary for generation, energy storage, transmission, distribution, and the retail supply of electricity;\n**(C)**\nmay sell electricity at retail to eligible CREU customers, subject to the condition that the system is physically islanded from\u2014\n**(i)**\nall regulated utilities;\n**(ii)**\nthe bulk-power system; and\n**(iii)**\nthe Bulk Electric System (as defined by the Electric Reliability Organization);\n**(D)**\nengages in any combination of\u2014\n**(i)**\ngenerating electricity;\n**(ii)**\ntransmitting electricity;\n**(iii)**\ndistributing electricity; or\n**(iv)**\nselling electricity at retail to consumers;\n**(E)**\nis not connected to the bulk-power system or any other electric transmission or distribution system for primary or backup supply; and\n**(F)**\noperates independently of any public utility.\n**(3) Electric Reliability Organization**\nThe term Electric Reliability Organization has the meaning given the term in section 215(a) of the Federal Power Act ( 16 U.S.C. 824o(a) ).\n**(4) Eligible CREU customer**\nThe term eligible CREU customer means any entity that\u2014\n**(A)**\npurchases electricity at retail from a consumer-regulated electric utility;\n**(B)**\nreceives electric service exclusively through facilities owned, constructed, or operated by consumer-regulated electric utilities; and\n**(C)**\nis located within premises that are physically islanded from\u2014\n**(i)**\nall regulated utilities;\n**(ii)**\nthe bulk-power system; and\n**(iii)**\nthe Bulk Electric System (as defined by the Electric Reliability Organization).\n**(5) Reliability standard**\nThe term reliability standard has the meaning given the term in section 215(a) of the Federal Power Act ( 16 U.S.C. 824o(a) ).\n#### 3. Federal Power Act exemption\nA consumer-regulated electric utility\u2014\n**(1)**\nshall be exempt from regulation under the Federal Power Act ( 16 U.S.C. 791a et seq. ), including with respect to\u2014\n**(A)**\nrate regulation;\n**(B)**\ncorporate or financial oversight;\n**(C)**\ntransmission or distribution regulation;\n**(D)**\nreliability standards under section 215 of that Act ( 16 U.S.C. 824o );\n**(E)**\ninterconnection requirements;\n**(F)**\nparticipation in regional transmission planning or cost allocation; and\n**(G)**\nmerger, consolidation, acquisition, or disposition approval under section 203 of that Act ( 16 U.S.C. 824b );\n**(2)**\nshall not be considered to be a public utility for purposes of that Act;\n**(3)**\nshall not be considered to be a part of\u2014\n**(A)**\nthe bulk-power system; or\n**(B)**\nthe Bulk Electric System (as defined by the Electric Reliability Organization); and\n**(4)**\nshall not be required to register with the Electric Reliability Organization or comply with reliability standards, unless the consumer-regulated electric utility voluntarily elects to connect to the bulk-power system.\n#### 4. Exemption of new CREUs from FERC and DOE regulation\n##### (a) In general\nNotwithstanding any other provision of law, a consumer-regulated electric utility that begins operations on or after the date of enactment of this Act shall be exempt from Federal regulation with respect to matters under the jurisdiction of the Federal Energy Regulatory Commission or the Secretary of Energy, including\u2014\n**(1)**\nall reliability standards; and\n**(2)**\nall other standards, rules, regulations, or other requirements established, administered, or enforced under\u2014\n**(A)**\nsection 215 of the Federal Power Act ( 16 U.S.C. 824o );\n**(B)**\nany other provision of that Act; or\n**(C)**\nany other provision of Federal law (including regulations).\n##### (b) Beginning of operations\nFor purposes of subsection (a), the date on which a consumer-regulated electric utility begins operations is the date on which the consumer-regulated electric utility first generates, transmits, distributes, or sells electricity.\n##### (c) Termination of exemption\nIf a consumer-regulated electric utility elects to connect to any portion of the bulk-power system or any other electric transmission or distribution system for primary or backup supply, the consumer-regulated electric utility shall, immediately on making that connection\u2014\n**(1)**\ncease being a consumer-regulated electric utility; and\n**(2)**\nbecome subject to all Federal regulation applicable to the consumer-regulated electric utility from which the consumer-regulated electric utility was exempt under subsection (a).\n#### 5. PURPA exemption\nSection 210 of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 824a\u20133 ) is amended by adding at the end the following:\n(o) Consumer-Regulated electric utilities (1) In general Nothing in this section applies to a consumer-regulated electric utility (as defined in section 2 of the DATA Act of 2026 ). (2) Exemption A consumer-regulated electric utility (as defined in section 2 of the DATA Act of 2026 ) shall not be required to interconnect with, purchase from, or sell to an electric utility under this section. .\n#### 6. PUHCA exemption\nSection 1268 of the Public Utility Holding Company Act of 2005 ( 42 U.S.C. 16456 ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking Except and inserting the following:\n(a) In general Except ; and\n**(2)**\nby adding at the end the following:\n(b) Consumer-Regulated electric utilities No provision of this subtitle shall apply to any holding company solely by reason of its ownership or control of a consumer-regulated electric utility (as defined in section 2 of the DATA Act of 2026 ). .\n#### 7. Facilities located within public rights-of-way\n##### (a) In general\nA consumer-regulated electric utility may construct and operate facilities within existing public rights-of-way, subject to the same permitting, restoration, and public-safety requirements applicable to a public utility (as defined in section 201(e) of the Federal Power Act ( 16 U.S.C. 824(e) )).\n##### (b) Limitation\nNotwithstanding subsection (a), the review of an application for the construction or operation of a facility within an existing public right-of-way by a consumer-regulated electric utility shall be confined exclusively to the adequacy of\u2014\n**(1)**\nright-of-way restoration; and\n**(2)**\nstorm-response planning.",
      "versionDate": "2026-04-21",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-01-07",
        "text": "Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "3585",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "DATA Act of 2026",
      "type": "S"
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
        "name": "Energy",
        "updateDate": "2026-05-04T14:09:21Z"
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
      "date": "2026-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8400ih.xml"
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
      "title": "DATA Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-27T12:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DATA Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-27T12:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Decentralized Access to Technology Alternatives Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-27T12:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Power Act to exempt consumer-regulated electric utilities from Federal regulation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-27T12:03:29Z"
    }
  ]
}
```
