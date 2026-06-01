# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6832?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6832
- Title: PACK Act
- Congress: 119
- Bill type: HR
- Bill number: 6832
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-05-30T08:05:55Z
- Update date including text: 2026-05-30T08:05:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6832",
    "number": "6832",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "W000814",
        "district": "14",
        "firstName": "Randy",
        "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
        "lastName": "Weber",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "PACK Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:55Z",
    "updateDateIncludingText": "2026-05-30T08:05:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T14:00:40Z",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "AL"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "NC"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "CA"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "NY"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "FL"
    },
    {
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "OH"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "IA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "TX"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "GA"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "OH"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "WI"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "ID"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6832ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6832\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Mr. Weber of Texas introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Trade Commission Act to include requirements for recyclable, compostable, and reusable claims for packaging for a consumer product, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Packaging and Claims Knowledge Act of 2025 or the PACK Act .\n#### 2. Requirements for recyclable, compostable, and reusable claims for packaging for a consumer product\nThe Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) is amended by inserting after section 26 the following:\n27. Recyclable, compostable, and reusable claims for packaging for a consumer product (a) Compostable, Recyclable, and Reusable Claims (1) Recyclable Claims (A) Deceptive claims prohibited A person may not claim that packaging for a consumer product is recyclable if the packaging is not recyclable. (B) Qualifying claims of recycling required Except as provided in subparagraph (C), a person shall clearly and prominently qualify the description of a recyclable claim by informing consumers about the availability of recycling programs and collection sites where the item is sold\u2014 (i) by including the percentage of consumers or communities that have access to recycle the packaging for the consumer product; or (ii) by including qualifications that vary in strength depending on availability. (C) Exemption from qualified claims for availability A person is exempt from the requirement of subparagraph (B) if\u2014 (i) a recycling program or facility is available to a substantial majority of consumers or communities in which the consumer product is sold; and (ii) the entire consumer product package, excluding any minor incidental component, is recyclable. (D) Not recyclable The following circumstances are not considered recyclable for purposes of this paragraph: (i) A case in which any component of the consumer product packaging significantly limits the ability to recycle the packaging of the consumer product. (ii) A case in which packaging for a consumer product that is made from recyclable material, but, because of the shape, size, or some other attribute of the consumer product packaging, is not accepted in recycling programs. (2) Compostable Claims for Consumer Product Packaging (A) Deceptive claims prohibited A person may not make a claim that packaging for a consumer product is compostable if the packaging is not compostable. (B) Evidence required A person that claims packaging for a consumer product is compostable shall have competent and reliable scientific evidence that the packaging is compostable. (C) Qualifying claim of compostability required A person shall clearly and prominently include a qualifying description on any claim that the packaging for a consumer product is compostable to the extent necessary to inform consumers about the ability of the packaging to be composted if\u2014 (i) the consumer product packaging cannot be composted safely or in a timely manner in a home compost pile or device; (ii) the claim misleads reasonable consumers about the environmental benefit provided when the consumer product packaging is disposed of in a landfill; or (iii) municipal or institutional composting facilities are not available where the item is sold to a substantial majority of consumers or communities. (3) Reusable Claims for Consumer Product Packaging (A) Deceptive claims prohibited A person may not claim that packaging for a consumer product is reusable if the packaging is not reusable. (B) Means for reuse required A person may not make an unqualified reusable claim for consumer product packaging unless the person provides the means for reusing the packaging through\u2014 (i) providing a system for the collection and reuse of the packaging; or (ii) offering for sale a product that consumers can purchase to reuse the original packaging. (4) Use of Resin Identification Codes Consumer product packaging that is not eligible to bear a compostable, recyclable, or reusable claim shall not bear a resin identification code that is surrounded by three chasing, triangulated arrows, except that such packaging may bear a resin identification code that is surrounded by an equilateral triangle, consistent with ASTM International Standard D7611/D7611M\u201319. (5) Third-party Certification A person may not make a claim that packaging for a consumer product is compostable, recyclable, or reusable unless an accredited third-party certification body has certified such claim. (6) Rule of construction This section may not be construed to apply to packaging that is not for a consumer product. (b) Commission Guidance (1) In General Not later than two years after the date of the enactment of this section, the Commission shall issue guidance for a person to be in compliance with subsection (a) that includes the following: (A) Criteria for accreditation bodies to consider in accrediting third party certification bodies, including whether\u2014 (i) a third party certification body meets the requirements of ISO/IEC 17065:2012, including any amendment; and (ii) such body is qualified to certify compostable, recyclable, and reusable claims for consumer product packaging consistent with the requirements described in this section. (B) A consideration of different types of consumer product packaging materials, including paper, plastic, glass, metal, or a combination thereof. (C) A consideration of different colors, shapes, and sizes of consumer product packaging materials. (2) Rules and regulations prohibited Notwithstanding section 6(g), the Commission may not issue any binding rule or regulation under this section. (3) Personnel and Formation of Advisory Council In issuing guidance and in administering the provisions of this section the Commission shall\u2014 (A) work with and consider input from the Administrator to leverage the knowledge of the Environmental Protection Agency on issues related to waste and product lifecycle management, including on issues relating to the use and management of compostable, recyclable, and reusable consumer product packaging; and (B) not later than one year after the date of the enactment of this section, the Commission shall establish an advisory council that meets at least annually and is comprised of subject matter and technical experts representing industry stakeholders, including packaging material suppliers, manufacturers of consumer products, and entities involved in the collection and management of discarded consumer product packaging. (c) Enforcement by Federal Trade Commission (1) Unfair and Deceptive Acts or Practices A violation of this section shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B). (2) Powers of the Commission (A) In General The Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of this section were incorporated into and made a part of this section. (B) Privileges and Immunities Any person that violates this section shall be subject to the penalties, and entitled to the privileges and immunities, provided in this Act. (C) Compelled Claims The Commission may not compel, require, or otherwise mandate a person to make a claim that consumer product packaging is compostable, recyclable, or reusable. (3) Preemption A State and political subdivision of a State may not establish, enforce, or continue in effect any provision of law or a legal requirement that is not identical with any requirement under this section. (d) Definitions In this section: (1) Accreditation The term accreditation means a determination by an accreditation body that a third-party certification body meets the applicable requirements of ISO/IEC 17065:2012, including any amendment, and is qualified to certify compostable, recyclable, and reusable claims for consumer product packaging. (2) Accreditation Body The term accreditation body means a person that performs accreditation of third-party certification bodies and is in compliance with ISO/IEC 17011:2017, including any amendment. (3) Accredited third-party certification body The term accredited third-party certification body means a third-party certification body that an accreditation body has determined meets the requirements of ISO/IEC 17065:2012, including any amendment, and is qualified to certify and is certifying compostable, recyclable, and reusable claims for consumer product packaging. (4) Administrator The term Administrator means the Administrator of the Environmental Protection Agency. (5) Claim The term claim \u2014 (A) means any statement or representation that is conveyed through any means, including through writing, symbols, marks, graphics, or electronic or digital links; and (B) does not include any instruction regarding how to recycle, compost, or reuse packaging. (6) Commission The term Commission means the Federal Trade Commission. (7) Compostable The term compostable means the packaging is designed to be associated with materials collected for composting that meets ASTM or equivalent industrial compostability standards, and similarly appropriate standards for the case of home compostability, and is capable of breaking down into, or otherwise becoming part of, stable and mature compost at an appropriate industrial composting facility, or in a home compost pile or device. (8) Consumer Product The term consumer product means\u2014 (A) any tangible product; (B) that is\u2014 (i) sold, offered for sale, or distributed in the United States, or intended to be sold, offered for sale, or distributed in the United States; and (ii) to a person that is an individual consumer and not a trust, firm, joint stock company, corporation (including a government corporation), partnership, association, State, municipality, commission, political subdivision of a State, or any interstate body, including any department, agency, and instrumentality of the United States; and (C) which is normally used or consumed by an individual consumer, including for personal, recreational, educational, family, household, or personal property maintenance or care purposes, including any product that is ordinarily available for purchase by an individual consumer. (9) Packaging The term packaging means any material that is used for the containment, protection, handling, delivery, and presentation of a tangible product that is sold, offered for sale, or distributed in the United States. (10) Person The term person means any individual, partnership, corporation, trust, estate, cooperative, association, or other entity. (11) Recyclable The term recyclable means that packaging can be collected, sorted, reprocessed, and ultimately reused in manufacturing or to make another item. (12) Reusable The term reusable means the packaging is designed to accomplish within the life cycle of the packaging more than one trip, rotation, or use for the same purpose for which the packaging was primarily designed. (13) Substantial majority The term substantial majority means 60 percent or more. (14) Third-party Certification Body The term third-party certification body means a person that is eligible to be considered for accreditation to evaluate, develop, and certify compostable, recyclable, and reusable claims for consumer product packaging. .",
      "versionDate": "2025-12-17",
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
        "name": "Commerce",
        "updateDate": "2026-03-19T19:44:56Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6832ih.xml"
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
      "title": "PACK Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T03:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PACK Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-18T03:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Packaging and Claims Knowledge Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-18T03:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Trade Commission Act to include requirements for recyclable, compostable, and reusable claims for packaging for a consumer product, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T03:03:26Z"
    }
  ]
}
```
