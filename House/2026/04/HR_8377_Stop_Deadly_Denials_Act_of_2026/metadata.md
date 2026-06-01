# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8377?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8377
- Title: Stop Deadly Denials Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8377
- Origin chamber: House
- Introduced date: 2026-04-20
- Update date: 2026-04-28T15:07:01Z
- Update date including text: 2026-04-28T15:07:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-20: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-04-20: Introduced in House

## Actions

- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-20",
    "latestAction": {
      "actionDate": "2026-04-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8377",
    "number": "8377",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000389",
        "district": "17",
        "firstName": "Ro",
        "fullName": "Rep. Khanna, Ro [D-CA-17]",
        "lastName": "Khanna",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Stop Deadly Denials Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-28T15:07:01Z",
    "updateDateIncludingText": "2026-04-28T15:07:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-20",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-20",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-20",
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
          "date": "2026-04-20T16:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-04-20T16:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "WA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "TN"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "MI"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "IL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "DC"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8377ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8377\nIN THE HOUSE OF REPRESENTATIVES\nApril 20, 2026 Mr. Khanna (for himself, Ms. Jayapal , Mr. Cohen , Mrs. Dingell , Mr. Jackson of Illinois , Ms. Norton , and Mr. Pocan ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to prohibit the use of prior authorization under Medicare Advantage plans, to amend title XI of the Social Security Act to limit the implementation of payment models testing prior authorization under traditional Medicare, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Deadly Denials Act of 2026 .\n#### 2. Prohibiting prior authorization requirements in Medicare Advantage\n##### (a) In general\nSection 1852 of the Social Security Act ( 42 U.S.C. 1395w\u201322 ) is amended by adding at the end the following new subsection:\n(o) Limitation on prior authorization (1) In general Subject to paragraph (2) , for plan years beginning on or after January 1, 2027, a Medicare Advantage plan may not impose any prior authorization requirement with respect to any specified item or service. (2) Exception Paragraph (1) shall not apply with respect to a specified item or service for a plan year in the case that, during such year, such item or service is subject to prior authorization pursuant to subsection (t)(2)(F) or (aa) of section 1833, subsection (a)(15), (l)(16), (q)(6), or (u)(4) of section 1834, or any other provision of part A or part B of this title. (3) Specified item or service defined For purposes of this subsection, the term specified item or service means, with respect to a Medicare Advantage plan, any item or service for which benefits are available under such plan that is not\u2014 (A) a covered part D drug; or (B) a supplemental health care benefit (as described in subsection (a)(3)). .\n##### (b) Permitting intermediate sanctions in the case of noncompliance\nSection 1857(g)(1) of the Social Security Act ( 42 U.S.C. 1395w\u201327(g)(1) ) is amended\u2014\n**(1)**\nin subparagraph (J), by striking or at the end;\n**(2)**\nin subparagraph (K), by striking subparagraphs (A) through (J) and inserting subparagraphs (A) through (K) ;\n**(3)**\nby redesignating subparagraph (K) as subparagraph (L); and\n**(4)**\nby inserting after subparagraph (J) the following new subparagraph:\n(K) imposes a prior authorization requirement with respect to an item or service in violation of section 1852(o); or .\n##### (c) Conforming change\nSection 1852(c)(1)(G) of the Social Security Act ( 42 U.S.C. 1395w\u201322(c)(1)(G) ) is amended\u2014\n**(1)**\nin the subparagraph heading, by striking Prior authorization and inserting Review ; and\n**(2)**\nby inserting for plan years ending before January 1, 2027, after Rules regarding prior authorization .\n#### 3. Limiting implementation of Center for Medicare and Medicaid Innovation models testing prior authorization under traditional Medicare\n##### (a) Prohibiting implementation of WISeR model\nThe Secretary of Health and Human Services may not implement the innovative payment and service delivery model described in the notice titled Medicare Program; Implementation of Prior Authorization for Select Services for the Wasteful and Inappropriate Services Reduction (WISeR) Model (90 Fed. Reg. 28749 (July 1, 2025)), or any substantially similar model.\n##### (b) Limiting implementation of future CMI models testing prior authorization under traditional Medicare\nSection 1115A(b)(2) of the Social Security Act ( 42 U.S.C. 1315a(b)(2) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking The Secretary shall select and inserting Subject to the limitation under subparagraph (D), the Secretary shall select ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(D) Limitation on models to be tested Beginning on the date of the enactment of this subparagraph, the Secretary may not select a model to be tested under subparagraph (A) if such model\u2014 (i) would provide for the implementation of prior authorization with respect to items or services for which payment may be made under part A or part B of title XVIII; and (ii) would provide for\u2014 (I) issuing any denial of coverage or payment that\u2014 (aa) is based on a decision made through the use of artificial intelligence, machine learning, algorithmic-derived decision logic, or any other similar technological process, without review and approval of such denial; and (bb) has not been individually reviewed and approved by a physician on the basis of the physician\u2019s independent medical judgment, taking into account relevant documentation provided by the individual receiving such items or services or the provider furnishing such items or services; or (II) the processing of requests for prior authorization by any entity other than a medicare administrative contractor with a contract under section 1874A. .\n##### (c) Requiring notice and comment for all future CMI models\nSection 1115A(b)(2)(A) of the Social Security Act ( 42 U.S.C. 1315a(b)(2)(A) ), as amended by subsection (b) , is further amended by adding at the end the following new sentence: Beginning January 1, 2027, a model may only be selected under this subparagraph after notice and opportunity for public comment. .",
      "versionDate": "2026-04-20",
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
        "name": "Health",
        "updateDate": "2026-04-28T15:07:01Z"
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
      "date": "2026-04-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8377ih.xml"
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
      "title": "Stop Deadly Denials Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T09:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Deadly Denials Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T09:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to prohibit the use of prior authorization under Medicare Advantage plans, to amend title XI of the Social Security Act to limit the implementation of payment models testing prior authorization under traditional Medicare, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T09:33:27Z"
    }
  ]
}
```
