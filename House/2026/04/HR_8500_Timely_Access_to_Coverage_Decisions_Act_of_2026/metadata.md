# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8500?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8500
- Title: Timely Access to Coverage Decisions Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8500
- Origin chamber: House
- Introduced date: 2026-04-27
- Update date: 2026-05-19T20:20:40Z
- Update date including text: 2026-05-19T20:20:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-27: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-27 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-04-27: Introduced in House

## Actions

- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-27 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-27",
    "latestAction": {
      "actionDate": "2026-04-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8500",
    "number": "8500",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000628",
        "district": "2",
        "firstName": "Neal",
        "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
        "lastName": "Dunn",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Timely Access to Coverage Decisions Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-19T20:20:40Z",
    "updateDateIncludingText": "2026-05-19T20:20:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-27",
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
      "actionDate": "2026-04-27",
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
      "actionDate": "2026-04-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-27",
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
          "date": "2026-04-27T16:04:25Z",
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
          "date": "2026-04-27T16:04:20Z",
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
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8500ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8500\nIN THE HOUSE OF REPRESENTATIVES\nApril 27, 2026 Mr. Dunn of Florida (for himself, Ms. Barrag\u00e1n , and Ms. Tenney ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to ensure timely review of local coverage determination requests under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Timely Access to Coverage Decisions Act of 2026 .\n#### 2. Ensuring timely review of local coverage determination requests under the Medicare program\n##### (a) In general\nSection 1862(l)(5) of the Social Security Act ( 42 U.S.C. 1395y(l)(5) ) is amended by adding at the end the following new subparagraph:\n(E) Timeframe for decisions on requests for local coverage determinations (i) In general The Secretary shall require each Medicare administrative contractor that receives a formal LCD request on or after the date that is 90 days after the date of enactment of this subparagraph to determine whether such request is a complete request or an incomplete request not later than 60 days after such contractor receives such request. (ii) Notification with respect to incomplete requests In the case that a Medicare administrative contractor makes a determination described in clause (i) with respect to a formal LCD request that such request is incomplete, such contractor shall, not later than 60 days after the date on which such contractor received such request, transmit to the entity that submitted such request a written notification of such determination that includes a specification of each item of additional information needed to make such request complete. (iii) Decision timeline for complete requests In the case that a Medicare administrative contractor makes a determination described in clause (i) with respect to a formal LCD request that such request is complete, such contractor shall, not later than 1 year after the date on which such contractor received such request, take the actions described in clauses (i) and (ii) of subparagraph (D). (iv) Formal LCD request defined In this subparagraph, the term formal LCD request means a document that identifies itself as a formal request for a local coverage determination. .\n##### (b) Reconsideration requests\nSection 1862(l)(5) of the Social Security Act ( 42 U.S.C. 1395y(l)(5) ), as amended by subsection (a) , is further amended by adding at the end the following new subparagraphs:\n(F) Timeframe for decisions on reconsideration requests for local coverage determinations (i) In general The Secretary shall require each Medicare administrative contractor that receives a formal reconsideration request on or after the date that is 90 days after the date of enactment of this subparagraph to determine whether such request is a complete request or an incomplete request not later than 60 days after such contractor receives such request. (ii) Notification with respect to incomplete requests In the case that a Medicare administrative contractor makes a determination described in clause (i) with respect to a formal reconsideration request that such request is incomplete, such contractor shall, not later than 60 days after the date on which such contractor received such request, transmit to the entity that submitted such request a written notification of such determination that includes a specification of each item of additional information needed to make such request complete. (iii) Decision timeline for complete requests In the case that a Medicare administrative contractor makes a determination described in clause (i) with respect to a formal reconsideration request that such request is complete, such contractor shall, not later than 1 year after the date on which such contractor received such request, take the actions described in clauses (i) and (ii) of subparagraph (D). (iv) Definitions In this subparagraph: (I) Formal reconsideration request The term formal reconsideration request means, with respect to a Medicare administrative contractor, a document that\u2014 (aa) identifies itself as a formal request for reconsideration of part or all of a finalized local coverage determination made by such contractor with respect to a geographic area; and (bb) is submitted by an interested party. (II) Interested party The term interested party means, with respect to a local coverage determination made by a Medicare administrative contractor with respect to a geographic area\u2014 (aa) an individual entitled to benefits under part A or enrolled under part B who resides in, or receives items or services in, such area; (bb) a provider of services or supplier that, in such area, furnishes, provides, or supplies items or services that are subject to such determination; or (cc) any entity that the Secretary determines to be an interested party in such area. (G) Agency review of reconsideration decision Upon the request of an interested party (as defined in subparagraph (F)(iv)), the Secretary shall review the final determination (as defined in subparagraph (D)(ii)) made by a Medicare administrative contractor following a complete formal reconsideration request made under subparagraph (F). Such review shall include an analysis of whether\u2014 (i) the determination did not apply, or inaccurately interpreted, qualifying evidence (as defined in subparagraph (D)(iv)) relevant to such determination; (ii) the determination used language that exceeded the scope of the intended purpose of the determination; (iii) the determination was incorrect in its determination of whether such item or service is reasonable and necessary for the diagnosis or treatment of illness or injury under section 1862(a)(1)(A); (iv) the determination failed to describe, with respect to such an item or service, the clinical conditions to be used for purposes of determining whether such item or service is reasonable and necessary for the diagnosis or treatment of illness or injury under section 1862(a)(1)(A); (v) the determination does not apply with respect to items or services to which it was intended to apply; or (vi) the determination conflicts with any other law, rule, regulation, or national coverage determination, as determined by the Secretary. .\n##### (c) Development process for specified LCDs\nSection 1862(l)(5)(D) of the Social Security Act ( 42 U.S.C. 1395y(l)(5)(D) ) is amended to read as follows:\n(D) Process for issuing specified local coverage determinations (i) In general In the case of a specified local coverage determination (as defined in clause (iii)) within an area by a Medicare administrative contractor, such contractor must take the following actions with respect to such determination before such determination may take effect: (I) Publish on the public internet website of the Centers for Medicare & Medicaid Services commonly referred to as the Medicare Coverage Database (or a successor website) and on the public internet website of the Medicare administrative contractor a proposed version of the specified local coverage determination (in this subparagraph referred to as a draft determination ), any related coding or billing information, a written rationale for the draft determination, and a description of all evidence relied upon and considered by the contractor in the development of the draft determination. (II) Not later than 60 days after the date on which the Medicare administrative contractor publishes the draft determination in accordance with subclause (I)\u2014 (aa) convene one or more open, public meetings to review the draft determination, and, with respect to each such meeting, make available means for the public to attend such meeting remotely, and make the planned agenda for such meeting publicly accessible at least 14 days in advance; (bb) receive comments with respect to the draft determination; and (cc) secure the advice of an expert panel, which shall include\u2014 (AA) 1 or more physicians; (BB) 1 or more members of the Contractor Advisory Committee (as described in chapter 13 of the Medicare Program Integrity Manual, as in effect on February 12, 2019); and (CC) 1 or more entities advocating on behalf of one or more individuals entitled to benefits under part A or enrolled under part B. (III) With respect to each meeting convened pursuant to subclause (II)(aa), post on the public internet website of the contractor, not later than 14 days after such meeting is convened, a record of such meeting, which may include a video or audio recording of the meeting. (IV) Provide a period for submission of written public comment on such draft determination that begins on the date on which all records required to be posted with respect to such draft determination under subclause (III) are so posted and that is not fewer than 30 days in duration. (ii) Finalizing a specified local coverage determination (I) In general Subject to subclause (II) , a Medicare administrative contractor that has entered into a contract with the Secretary under section 1874A shall, before a specified local coverage determination (in this subparagraph referred to as the final determination ) takes effect, post on the Medicare Coverage Database and the public internet website of the contractor the following information: (aa) A response to public comments received and the relevant issues raised at meetings convened pursuant to clause (i)(II)(aa) with respect to the draft determination. (bb) The full text of all such public comments received. (cc) The rationale for the final determination. (dd) In the case that the Medicare administrative contractor considered qualifying evidence (as defined in clause (v)) in the development of the determination that was not described in the written notice provided pursuant to clause (i)(I), a description of such qualifying evidence. (ee) An effective date for the final determination that is not less than 45 days after the date on which such determination is so posted. (II) Logical outgrowth requirement Notwithstanding subclause (I) , a final determination may not take effect unless such determination is a logical outgrowth of the draft determination published under clause (i) . (iii) Specified local coverage determination defined For purposes of this subparagraph, the term specified local coverage determination means, with respect to the relevant geographic area\u2014 (I) a new local coverage determination; (II) a revised local coverage determination that makes a substantive revision to one or more existing local coverage determinations (such as by imposing new requirements with respect to coverage of the relevant item or service or by changing any coding or billing information related to such determination); or (III) any other local coverage determination specified by the Secretary pursuant to regulations. (iv) Qualifying evidence defined For purposes of this subparagraph, the term qualifying evidence means publicly available evidence of general acceptance by the medical community, such as published original research in peer-reviewed medical journals, systematic reviews and meta-analyses, evidence-based consensus statements, and clinical guidelines. .\n##### (d) Effective date\nThis section, and the amendments made by this section, shall apply beginning on the date that is 1 year after the date of the enactment of this section.",
      "versionDate": "2026-04-27",
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
        "updateDate": "2026-05-19T20:20:39Z"
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
      "date": "2026-04-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8500ih.xml"
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
      "title": "Timely Access to Coverage Decisions Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T09:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Timely Access to Coverage Decisions Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to ensure timely review of local coverage determination requests under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T09:18:39Z"
    }
  ]
}
```
