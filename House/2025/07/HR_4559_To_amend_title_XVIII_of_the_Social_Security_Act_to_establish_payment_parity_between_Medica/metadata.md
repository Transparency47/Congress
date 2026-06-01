# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4559?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4559
- Title: Prompt and Fair Pay Act
- Congress: 119
- Bill type: HR
- Bill number: 4559
- Origin chamber: House
- Introduced date: 2025-07-21
- Update date: 2026-04-10T08:06:15Z
- Update date including text: 2026-04-10T08:06:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-21: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-21 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-21: Introduced in House

## Actions

- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-21 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-21",
    "latestAction": {
      "actionDate": "2025-07-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4559",
    "number": "4559",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000399",
        "district": "37",
        "firstName": "Lloyd",
        "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
        "lastName": "Doggett",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Prompt and Fair Pay Act",
    "type": "HR",
    "updateDate": "2026-04-10T08:06:15Z",
    "updateDateIncludingText": "2026-04-10T08:06:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-21",
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
      "actionDate": "2025-07-21",
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
      "actionDate": "2025-07-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-21",
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
          "date": "2025-07-21T16:00:20Z",
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
          "date": "2025-07-21T16:00:15Z",
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
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "NC"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "MD"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "AL"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "TX"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "NC"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "PA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4559ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4559\nIN THE HOUSE OF REPRESENTATIVES\nJuly 21, 2025 Mr. Doggett (for himself and Mr. Murphy ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to establish payment parity between Medicare Advantage and fee-for-service Medicare, and to establish prompt payment requirements under Medicare Advantage.\n#### 1. Short title\nThis Act may be cited as the Prompt and Fair Pay Act .\n#### 2. Establishing payment parity between Medicare Advantage and fee-for-service Medicare\nSection 1857(e) of the Social Security Act ( 42 U.S.C. 1395w\u201327(e) ) is amended by adding at the end the following new paragraph:\n(6) Payment parity with fee-for-service Medicare Beginning with plan years beginning on or after January 1, 2027, a contract under this part shall require an MA organization to provide, in any contract between the organization and a provider or supplier, that payment for items and services furnished to an enrollee by such provider or supplier shall be in an amount that is not less than the amount of payment applicable on the date of service for such items and services under the original Medicare fee-for-service program under parts A and B, including cost-based payment methodologies. .\n#### 3. Protecting beneficiary access to care under Medicare Advantage by establishing enforceable prompt payment requirements and enhancing transparency regarding claims denials\n##### (a) Applying prompt payment requirements for items and services furnished by in-Network providers\n**(1) In general**\nSection 1857(f) of the Social Security Act ( 42 U.S.C. 1395w\u201327(f) ) is amended\u2014\n**(A)**\nin paragraph (1), in the header, by inserting Applicable with respect to out-of-network providers of services and suppliers after Requirement ;\n**(B)**\nin paragraph (2), by striking compliance with paragraph (1) and inserting compliance with paragraph (1) or (2) ;\n**(C)**\nby redesignating paragraphs (2) and (3) as paragraphs (3) and (4), respectively; and\n**(D)**\nby inserting after paragraph (1) the following new paragraph:\n(2) Requirement applicable with respect to in-network providers of services and suppliers (A) Prompt payment of clean claims (i) In general For contract years beginning on or after January 1, 2027, a contract entered into with an MA organization with respect to offering an MA plan under this part shall require that contracts and other agreements between such MA organization and providers of services and suppliers to furnish items and services to enrollees under such plan shall provide that payment shall, in accordance with the provisions of this paragraph, be issued, mailed, or otherwise transmitted, with respect to all clean claims submitted for such items and services furnished by such providers of services and suppliers to such enrollees, by not later than the applicable number of calendar days (as defined in clause (iii)) after the date on which the claim is received (as determined in accordance with clause (ii)). (ii) Date of receipt of claim For purposes of this paragraph, a claim is considered to have been received\u2014 (I) with respect to claims submitted electronically, on the date on which the claim is transferred; and (II) with respect to claims submitted otherwise, on the 5th day after the postmark date of the claim or the date specified in the time stamp of transmission. (iii) Applicable number of calendar days defined For purposes of this paragraph, the term applicable number of calendar days means\u2014 (I) with respect to claims submitted electronically, 14 days; and (II) with respect to claims submitted otherwise, 30 days. (B) Procedures and rules for determining whether claims are clean claims (i) Clean claim defined In this paragraph, the term clean claim means\u2014 (I) a claim that has no defect or impropriety (including any lack of any required substantiating documentation) or particular circumstance requiring special treatment that prevents timely payment from being made on the claim under this part; and (II) a claim that otherwise conforms to the clean claim requirements for equivalent claims under original Medicare. (ii) Claim deemed to be clean when timely notice of any deficiency is not provided For purposes of this paragraph, with respect to an MA organization and a provider of services or supplier with whom the MA organization has a contract to furnish items and services, a claim for such items and services furnished by such provider of services or supplier under such contract shall be deemed to be a clean claim if the MA organization does not provide notice to the provider of services or supplier of any deficiency in the claim\u2014 (I) with respect to claims submitted electronically, within 10 days after the date on which the claim is received; and (II) with respect to claims submitted otherwise, within 15 days after the date on which the claim is received. (iii) Required notifications and treatment of claims initially determined to not be clean claims For purposes of this paragraph, with respect to an MA organization and a provider of services or supplier with whom the MA organization has a contract to furnish items and services\u2014 (I) if the MA organization determines that a submitted claim for such items and services furnished by such provider of services or supplier under such contract is not a clean claim, the MA organization shall, not later than the end of the applicable period described in clause (ii), notify the provider of services or supplier of such determination and in such notification shall specify all defects or improprieties in the claim and shall list all additional information or documents necessary for the proper processing and payment of the claim, including detailed instructions for resubmission of claims, how to address each specified defect or impropriety, any formatting or coding guidance specific to the rejection reason, and how to contact the plan to obtain assistance with resubmission; and (II) in the case in which additional information is received pursuant to a notification under subclause (I) with respect to a claim described in such subclause, the claim shall be deemed to be a clean claim described in clause (i) if the MA organization does not provide notice to the provider of service or supplier of any defect or impropriety in the claim not later than 10 days of the date on which such additional information is received. (iv) Rule of construction A determination under this paragraph that a claim submitted by a provider of services or supplier is a clean claim shall not be construed as a positive determination regarding eligibility for payment under this title, nor is it an indication of government approval of, or acquiescence regarding, the claim submitted. The determination shall not relieve any party of civil or criminal liability with respect to the claim, nor does it offer a defense to any administrative, civil, or criminal action with respect to the claim. (C) Obligation to pay For purposes of this paragraph: (i) In general A claim submitted to an MA organization that is not paid or contested by the organization within the applicable number of calendar days (as defined in subparagraph (A)(iii)) after the date on which the claim is received (as determined in accordance with subparagraph (A)(ii)) shall be deemed to be a clean claim and shall be paid by the MA organization in accordance with subparagraph (A)(i). (ii) Electronic transfer of funds An MA organization shall pay all clean claims submitted electronically by electronic transfer of funds if the provider of services or supplier so requests or has so requested previously. In the case in which such payment is made electronically, remittance may be made by the MA organization electronically as well. (iii) Date of payment of claim Payment of a clean claim under this paragraph shall be considered to have been made on the date on which\u2014 (I) with respect to claims paid electronically, the payment is transferred; and (II) with respect to claims paid otherwise, the payment is submitted to the United States Postal Service or common carrier for delivery. (D) Interest payment (i) For purposes of this paragraph, subject to clause (ii), if payment is not issued, mailed, or otherwise transmitted within the applicable number of calendar days (as defined in subparagraph (A)(iii)) after a clean claim (with respect to which this paragraph applies) is received, the MA organization shall pay interest to the provider of services or supplier that submitted the claim at a rate equal to the weighted average of interest on 3-month marketable Treasury securities determined for such period, increased by 0.1 percentage point for the period beginning on the day after the required payment date and ending on the date on which payment is made (as determined under subparagraph (C)(iii)). Interest amounts paid under this subparagraph shall not be counted against the administrative costs of an MA plan for purposes of determining the medical loss ratio of the plan under subsection (e)(4). (ii) Authority not to charge interest The Secretary may provide that an MA organization is not charged interest under clause (i) in the case in which there are exigent circumstances, including natural disasters and other unique and unexpected events, that prevent the timely processing of claims. (E) Protecting the rights of claimants (i) In general Nothing in this paragraph shall be construed to prohibit or limit a claim or action not covered by the subject matter of this paragraph that any individual or organization has against a provider of services, supplier, or an MA organization. (ii) Anti-retaliation Consistent with applicable Federal and State laws, an MA organization shall not retaliate against an individual, provider of services, or supplier for exercising a right of action under this subparagraph. .\n**(2) Secretarial authority to enforce prompt payment requirement**\nSection 1857(g)(1) of the Social Security Act ( 42 U.S.C. 1395w\u201327(g)(1) ) is amended\u2014\n**(A)**\nin subparagraph (J), by striking at the end or ;\n**(B)**\nin subparagraph (K), by inserting or after the semicolon; and\n**(C)**\nby inserting after subparagraph (K) the following new subparagraph:\n(L) fails to comply with the provisions of subsection (f)(2); .",
      "versionDate": "2025-07-21",
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
        "updateDate": "2025-09-11T17:09:39Z"
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
      "date": "2025-07-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4559ih.xml"
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
      "title": "Prompt and Fair Pay Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T05:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prompt and Fair Pay Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to establish payment parity between Medicare Advantage and fee-for-service Medicare, and to establish prompt payment requirements under Medicare Advantage.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T05:18:40Z"
    }
  ]
}
```
