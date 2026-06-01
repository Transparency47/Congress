# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3004?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3004
- Title: USPS SERVES US Act
- Congress: 119
- Bill type: HR
- Bill number: 3004
- Origin chamber: House
- Introduced date: 2025-04-24
- Update date: 2025-12-10T09:05:39Z
- Update date including text: 2025-12-10T09:05:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-24: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-04-24: Introduced in House

## Actions

- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-24",
    "latestAction": {
      "actionDate": "2025-04-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3004",
    "number": "3004",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "G000546",
        "district": "6",
        "firstName": "Sam",
        "fullName": "Rep. Graves, Sam [R-MO-6]",
        "lastName": "Graves",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "USPS SERVES US Act",
    "type": "HR",
    "updateDate": "2025-12-10T09:05:39Z",
    "updateDateIncludingText": "2025-12-10T09:05:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
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
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-24",
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
          "date": "2025-04-24T15:02:30Z",
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
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "SC"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "KS"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3004ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3004\nIN THE HOUSE OF REPRESENTATIVES\nApril 24, 2025 Mr. Graves introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 39, United States Code, to modernize the Postal Service regulations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the USPS Services Enhancement and Regulatory Viability Expansion and Sustainability for the US Act or the USPS SERVES US Act .\n#### 2. Cost and efficiency reforms\n##### (a) In general\nSection 3622(d) of title 39, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)(A), by striking to be set by and all that follows and inserting the following:\nequal to the amount that is the percentage change in the Consumer Price Index for All Urban Consumers unadjusted for seasonal variation over the most recent available 12-month period preceding the date the Postal Service files notice of its intention to increase rates less\u2014 (i) 0.5 percent; or (ii) such other percentage as specified in an order by the Commission if such order describes the reasons of the Commission for selecting such other percentage and such order applies such other percentage with respect to only one such annual limitation; ; and\n**(2)**\nby amending paragraph (3) to read as follows:\n(3) Revisions In revising the system as permitted by subsection (a), the Postal Regulatory Commission shall make no change which would cause the revised system to be inconsistent with this section. .\n##### (b) Regulations\nNot later than 60 days after the date of the enactment of this Act, the Postal Regulatory Commission shall issue such regulations as are necessary to carry out section 3622(d)(1)(A) of title 39, United States Code, as amended by this section.\n#### 3. Sanctions for certain failures of service\n##### (a) In general\nSubchapter VII of chapter 36 of title 39, United States Code, is amended by adding at the end the following new section:\n3693. Sanctions. (a) In general If, pursuant to section 3653 or a complaint proceeding conducted pursuant to section 3662, the Postal Regulatory Commission determines that the Postal Service failed to meet a target established under section 3692 and that such failure is a covered failure, the Commission may reduce the maximum amount by which the Postal Service may adjust the rates for the market-dominant products affected by such failure under section 3622, except that such reduction may not cause such maximum amount to be less than zero. In making such determination, the Commission shall consider evidence of losses incurred by users of the product or products concerned as a result of the failure. (b) Applicability (1) In general A reduction under subsection (a) to the maximum amount by which the Postal Service may adjust the rates for a market-dominant product under section 3622 shall apply only with respect to\u2014 (A) the first implementation of such an adjustment for such market-dominant product occurring during the period beginning on the date on which the Postal Regulatory Commission makes such reduction and ending on the date on which Commission determines that the Postal Service is meeting the target established under section 3692 with respect to which the Commission made such reduction; and (B) each subsequent implementation of such an adjustment for such market-dominant product occurring during such period to the extent determined appropriate by the Commission. (2) Subsequent implementation determination In making the determination described in paragraph (1)(B) with respect to a reduction for a failure described in subsection (a), the Postal Regulatory Commission shall consider evidence of losses incurred by users of each product affected by such failure. (c) Covered failure defined In this section, the term covered failure means a failure to meet a target established under section 3692\u2014 (1) that is not the result of a natural disaster or another disruptive event the cause of which was outside the control of the Postal Service; (2) that has persisted for not less than one year; and (3) with respect to which the Postal Service does not have a credible plan for achieving and maintaining performance sufficient to meet the targeted level within a reasonable time. .\n##### (b) Clerical amendment\nThe table of sections for chapter 36 of title 39, United States Code, is amended by inserting after the item relating to section 3692 the following:\n3693. Sanctions. .\n#### 4. Improving change-in-service procedures\nSection 3661 of title 39, United States Code, is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nby striking When the and insert (1) When the ;\n**(B)**\nby striking advisory opinion and inserting a decision ; and\n**(C)**\nby adding at the end the following new paragraph:\n(2) (A) In the absence of a decision with respect to a proposal under paragraph (1), if the Commission determines that a plan or initiative of the Postal Service clearly indicates the need for a change described in such paragraph but such plan or initiative does not explicitly make such a change a purpose or goal of such plan or initiative, the Commission shall order the Postal Service to explain why the Postal Service determined that the Postal Service did not need to submit a proposal to the Commission under such paragraph with respect to such plan or initiative. (B) An order under subparagraph (A) pursuant to a determination of the Commission described in such subparagraph shall include an explanation of the reasoning for such determination. (C) (i) If the Commission determines that the explanation of the Postal Service provided pursuant to subparagraph (A) is not sufficient to support the determination of the Postal Service that the Postal Service did not need to submit a proposal to the Commission under paragraph (1) with respect to a plan or initiative, the Postal Service shall justify the change in the nature of postal services implied by the plan or initiative and, to the extent necessary, justify the underlying plan or initiative in a hearing before the Commission. (ii) Each hearing under clause (i) shall be conducted in accordance with sections 556 and 556 of title 5. (3) Each decision of the Postal Regulatory Commission under this subsection shall be transmitted to the Governors of the Postal Service. The Governors may accept the decision or, by unanimous written decision, reject the decision and adopt the original proposal of the Postal Service, in the case of a request by the Postal Service for a decision, or approve the plan or initiative found by the Commission to have required a decision under paragraph (2). The decision of the Governors shall be a final order for purposes of section 3663 of this title. If the Governors have not acted upon a Commission decision within 60 days of receiving it, the Commission decision will be deemed a final order for purposes of section 3663 of this title. ; and\n**(2)**\nin subsection (c)\u2014\n**(A)**\nby inserting designated pursuant to section 505 of this title after officer of the Commission ; and\n**(B)**\nby striking his judgment and inserting the judgment of such Commissioner .\n#### 5. One rate increase annually\nSection 3622(d)(1)(B) of title 39, United States Code, is amended by inserting after amounts the following: , except that rates may not change more frequently than once every 12 months .\n#### 6. Limit on underwater surcharges\nSection 3622(d)(2) of title 39, United States Code, is amended by adding at the end the following new subparagraph:\n(D) Use of rate authority for non-compensatory classes (i) Limitation Notwithstanding paragraph (1)(A), the Commission may authorize the Postal Service to increase the rates for a non-compensatory class in excess of annual limitation under paragraph (1)(A) if\u2014 (I) the change in the attributable cost (as such term is defined in section 3631) per piece of mail for such class does not exceed the annual limitation under paragraph (1)(A), as determined by the Commission using year-to-year comparable costing methodologies; (II) in the immediately preceding fiscal year, the Postal Service has\u2014 (aa) pursuant to section 3652 and without the use of any proxy data not approved by the Commission, directly measured and reported the compliance of the Postal Service with the targets established under section 3692 for each product in such class for such fiscal year; and (bb) met each such target for such fiscal year; and (III) no target described in subclause (II) for the immediately preceding fiscal year was reduced from the preceding fiscal year. (ii) Non-compensatory class defined In this subparagraph, the term non-compensatory class means a class of mail for which the attributable costs (as defined in section 3631(b)) of the Postal Service exceed revenues of the Postal Service attributable to such class of mail. .\n#### 7. Case-specific objectives\nSection 3622 of title 39, United States Code, is amended\u2014\n**(1)**\nin subsection (b), in the matter preceding paragraph (1), by inserting , and all of which shall be applied to each class or type of mail service and product after others ; and\n**(2)**\nin subsection (c), in the matter preceding paragraph (1), by inserting after such system, the following: or when evaluating whether a class or type of mail service or product complies with the applicable provisions of this chapter and the regulations issues under such provisions, .\n#### 8. Retained earnings from cost savings\nSection 3622(b)(5) of title 39, United States Code, is amended by inserting after retained earnings the following: resulting from improvements in efficiency or reductions in cost only .\n#### 9. Office of the Customer Advocate\n##### (a) In general\nSection 505 of title 39, United States Code, is amended to read as follows:\n505. Office of the Customer Advocate (a) In general The Postal Regulatory Commission shall establish in the Postal Regulatory Commission an Office of the Customer Advocate (in this section referred to as the Office ). (b) Representation (1) In general The Office shall represent the interests of the general public in all public proceedings of the Commission, including the interests of customers of market-dominant products and classes. (2) Rights and limits (A) In general The Office\u2014 (i) shall have the same right as any interested person to lodge a complaint with or petition the Commission, or otherwise seek to have the Commission initiate a public proceeding, including rulemakings; and (ii) is subject to the same ex parte rules and limitations as any other litigant with respect to communication with the Commission, Commissioners, and the advisory staff of the Commission. (B) Represent conflicting interest (i) In general The Office may represent conflicting interests of the general public in a public proceeding of the Commission to the extent that the head of the Office determines necessary for the Office to effectively represent the interests of the general public in such proceeding. (ii) Separate representatives If the Office is representing conflicting interests of the general public in a public proceeding of the Commission, the head of the Office shall ensure that such conflicting interests are represented by different individuals to the extent and in such manner as the head of the Office determines necessary for the Office to effectively represent the interests of the general public in such proceeding. (3) Office autonomy The Commission may not terminate or otherwise take adverse employment action against any employee of or individual detailed to the Office based on the representation of the interests of the general public by such employee or detailee as an employee of or detailee to the Office, respectively, in a public proceeding of the Commission, except for cause. (c) Research authority The Office may\u2014 (1) conduct research and policy development for the purposes of representing the interests of the general public, including research and policy development that is unrelated to a specific proceeding of the Commission; and (2) subject to the availability of funds, obtain the temporary or intermittent services of experts or consultants for such purposes. (d) Outside consultation The Office shall consult with outside persons and organizations the postal interests of which are relevant to the mission of the Office, including those persons and organizations that are actual or potential litigants before the Commission. (e) Rate and classification inquiry The Office shall inquire into the rates and classifications of competitive products only to the extent necessary to evaluate compliance with sections 3622(b)(8) and 3622(b)(9) of this title, subchapter II of chapter 36 of this title, and the regulations issued under such subchapter. (f) Office staff The Commission shall ensure that, to the extent practicable, the Office has employees of a sufficient quantity and quality for the Office to effectively carry out the responsibilities of the Office under this section, including by maximizing the duration of the detail of individuals detailed to the Office. .\n##### (b) Clerical amendment\nThe table of sections for chapter 5 of title 39, United States Code, is amended by striking the item relating to section 505 and inserting the following:\n505. Office of the Customer Advocate. .\n#### 10. Complaint process improvement\nSection 3662 of title 39, United States Code, is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the matter preceding subparagraph (A)\u2014\n**(I)**\nby striking The Postal and inserting With respect to a complaint received under subsection (a), the Postal ; and\n**(II)**\nby striking , within 90 days after receiving a complaint under subsection (a) ; and\n**(ii)**\nin subparagraph (A)\u2014\n**(I)**\nby striking clause (i) and inserting the following:\n(i) begin proceedings on such complaint\u2014 (I) immediately after the expiration of the period described in paragraph (3) if the Commission finds that such complaint raises material issues of fact or law and no motion described in clause (ii) with respect to such complaint is filed in such period; (II) immediately after the Commission denies all motions described in clause (ii) with respect to such complaint that were filed during the period described in paragraph (3) if the Commission finds that such complaint raises material issues of fact or law and all such motions are denied not later than 45 days after the date on which the Commission received such complaint under such subsection; or (III) not later than 45 days after the date on which the Commission receives such complaint under such subsection if subclause (I) and (II) do not apply with respect to such complaint; or ; and\n**(II)**\nin clause (ii)\u2014\n**(aa)**\nby inserting before issue the following: if the Commission finds that, after consideration of any motion asserting that such complaint raises no material issues of law or fact, that such complaint raises no such issue, upon making such finding ; and\n**(bb)**\nby inserting within 45 days after receiving such complaint under such subsection after dismissing the complaint ; and\n**(B)**\nby adding at the end the following new paragraph:\n(3) Prompt motions A motion described in subparagraph (A)(ii) with respect to a complaint may only be filed during the 25-day period beginning on date on which such complaint is filed, or during such shorter period as the Postal Regulatory Commission may prescribed by regulation. ; and\n**(2)**\nin subsection (c)\u2014\n**(A)**\nby striking or requiring and inserting requiring ; and\n**(B)**\nby inserting after competitive products the following: or, upon a finding that the Postal Service has unreasonably delayed the proceeding, ordering reimbursement consistent with section 3681 .\n#### 11. Reimbursement of unlawful rates; penalty for unreasonable delay\nSection 3681 of title 39, United States Code, is amended\u2014\n**(1)**\nby striking No mailer and inserting (a) No mailer ;\n**(2)**\nby striking through 3664 of this title, or is superseded by a lower rate or fee established under subchapter II of this chapter ; and\n**(3)**\nby adding at the end the following new subsection:\n(b) (1) (A) If the Postal Regulatory Commissions determines that a rate or fee for a product is unlawful in a review conducted pursuant to section 3653 of this title or in a complaint proceeding conducted pursuant to section 3662 of this title, the Commission shall order the price increase authority for such product and all other products in the class of mail containing such product to be reduced (but not below zero) for the next following price adjustment and each succeeding price adjustments until the amount of foregone revenue is equal to amount of revenue received by the Postal Service from the portion of such rate or fee that exceeded the lawful amount such rate or fee. (B) In this paragraph, the term foregone revenue means the difference between\u2014 (i) the revenue that the Postal Service would have received from the sale of the products subject to an order under subparagraph (A) during the period that the Postal Service is unable to increase the prices of such products pursuant to such order if\u2014 (I) the Commission had not issued such order; and (II) the rate or fee for the product with the unlawful rate or fee for which the Commission issued such order was the maximum lawful rate or fee for such product at the time the Commission issued such order; and (ii) the revenue the Postal Service receives from the sale of the products subject to such order during such period. (2) (A) In a complaint proceeding conducted pursuant to section 3662 of this title, if the Postal Regulatory Commission finds that the Postal Service has unreasonably delayed the proceeding, the Commission may order a reduction in the price increase authority for the product or products whose rate or fee it has determined to be unlawful to the extent that the unreasonable delay caused by the Postal Service has extended the time during which users of such product or products have paid the unlawful rate or fee. (B) A reduction under subparagraph (A) shall be in addition to any reduction under paragraph (1). (C) The Commission shall include in an order under subparagraph (A) with respect to the unreasonably delay of a proceeding an explanation of the basis for the determination of the Commission regarding the time such proceeding would have required absent such unreasonable delay. .\n#### 12. Mail volume system objective\nSection 3622(b) of title 39, United States Code, is amended\u2014\n**(1)**\nby redesignating paragraph (9) as paragraph (10); and\n**(2)**\nby inserting after paragraph (8) the following new paragraph:\n(9) To maintain and, to the extent practicable, increase the volume of market-dominant mail, with due regard to total contribution to the institutional costs of the Postal Service. .\n#### 13. New product definition criteria\nSection 3642(b)(3) of title 39, United States Code, is amended\u2014\n**(1)**\nin subparagraph (B), by striking and ;\n**(2)**\nin subparagraph (C), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(D) the importance of paragraphs (7), (8), and (11) of section 3622(c) of this title in the appropriate definition of market-dominant products. .\n#### 14. Mail volume estimation model\n##### (a) In general\nNot later than 120 days after the date of the enactment of this Act, the Postal Regulatory Commission shall develop a model for estimating the demand for postal services.\n##### (b) Independent development\nThe Commission may not consider any models for estimating demand developed by the Postal Service when developing the model required under this section.\n##### (c) Public comment\nIn developing the model required under this section, the Postal Regulatory Commission shall solicit and provide adequate opportunity for public comment regarding the model.\n##### (d) Regulations\nThe Postal Regulatory Commission may issue such regulations, after notice and comment in accordance with section 553 of title 5, United States Code, as the Commission determines necessary to develop the model required under this section.\n##### (e) Expert advisors\nThe Commission may obtain the temporary or intermittent services of experts or consultants to facilitate the development of the model required under this section.\n#### 15. Investment of the postal service retiree health benefits funds\nSection 8909a(c) of title 5, United States Code, is amended\u2014\n**(1)**\nby striking (c) The Secretary and inserting (c)(1) Subject to paragraph (2), the Secretary ; and\n**(2)**\nby adding at the end the following:\n(2) (A) The Secretary of the Treasury shall immediately invest a specified percentage of the Fund, using one or more qualified professional asset managers, in index funds modeled after those established under subparagraphs (B), (C), (D), and (E) of section 8438(b)(1). The Secretary shall ensure, to the maximum extent practicable, that the investment replicates the performance of the longest-term target date asset allocation investment fund established by the Federal Retirement Thrift Investment Board. (B) In exercising authority under subparagraph (A), including in the selection of specific qualified professional asset managers and in the development of specific investment guidelines to meet the requirement of such subparagraph, the Secretary shall consult with the Postal Service Retiree Health Benefits Fund Investment Committee. (C) (i) There is established a Postal Service Retiree Health Benefits Fund Investment Committee that shall consist of\u2014 (I) the Secretary; (II) the Chair of the Board of Governors of the United States Postal Service; (III) the Chairman of the Federal Retirement Thrift Investment Board; and (IV) two members, appointed by the President, who\u2014 (aa) shall represent the interests of Postal Service employees and annuitants; (bb) have experience and expertise in the management of financial investments and Postal Service employee benefits; and (cc) shall serve for a term of 3 years. (ii) Subsections (b)(1) and (c)(2) of section 8477 shall apply with respect to the Postal Service Retiree Health Benefits Fund Investment Committee and each member of the Postal Service Retiree Health Benefits Fund Investment Committee in the same manner as such subsections apply to a fiduciary with respect to the Thrift Savings Fund. (D) (i) The Secretary shall annually engage an independent qualified public accountant (as defined in section 8439) to audit and provide a report on the financial statements of the investments made pursuant to subparagraph (A). (ii) Not later than 180 days after the end of each fiscal year beginning after the date of the enactment of this paragraph, the Secretary shall submit to Congress an annual management report regarding the Fund that includes\u2014 (I) a statement of financial position; (II) a statement of operations; (III) a statement of cash flows; (IV) a statement on internal accounting and administrative control systems; (V) the most recent report resulting from an audit of the financial statements of the investments conducted under clause (i); and (VI) any other comments and information the Secretary determines necessary to inform the Congress about the operations and financial condition of the investments. (E) In this paragraph\u2014 (i) the term specified percentage means 25 percent of the currently available portions of the Fund as are not immediately required for payments from the Fund, except that the Postal Service Retiree Health Benefits Fund Investment Committee may specify a higher percentage, not to exceed 30 percent, not earlier than 5 years after the date of enactment of the Postal Service Financial Improvement Act of 2019, and as appropriate thereafter; and (ii) the term qualified professional asset manager has the meaning given that term in section 8438(a). .",
      "versionDate": "2025-04-24",
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
        "updateDate": "2025-05-29T18:03:12Z"
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
      "date": "2025-04-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3004ih.xml"
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
      "title": "USPS SERVES US Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T08:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "USPS SERVES US Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T08:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "USPS Services Enhancement and Regulatory Viability Expansion and Sustainability for the US Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T08:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 39, United States Code, to modernize the Postal Service regulations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T08:18:21Z"
    }
  ]
}
```
