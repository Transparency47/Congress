# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2435?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2435
- Title: Save Our Small Farms Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2435
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2026-03-19T08:07:17Z
- Update date including text: 2026-03-19T08:07:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2435",
    "number": "2435",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001081",
        "district": "5",
        "firstName": "Jahana",
        "fullName": "Rep. Hayes, Jahana [D-CT-5]",
        "lastName": "Hayes",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Save Our Small Farms Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-19T08:07:17Z",
    "updateDateIncludingText": "2026-03-19T08:07:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-18",
      "committees": {
        "item": {
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-18T21:11:00Z",
              "name": "Referred to"
            }
          },
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CT"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CT"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CT"
    },
    {
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CT"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "NY"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2435ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2435\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mrs. Hayes (for herself, Mr. Larson of Connecticut , Mr. Courtney , Ms. DeLauro , and Mr. Himes ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Federal Agriculture Improvement and Reform Act of 1996 to assist farmers relying on the noninsured crop disaster assistance program by lowering the cost of purchasing coverage, reducing paperwork burdens, and increasing payouts under that program, and to incentivize farmers to transition gradually to a comprehensive insurance policy under the whole farm risk management insurance plan by offering progressive premium discounts on a commitment to purchase a whole farm plan of insurance.\n#### 1. Short title\nThis Act may be cited as the Save Our Small Farms Act of 2025 .\n#### 2. Administration and operation of noninsured crop assistance program\nSection 196 of the Federal Agriculture Improvement and Reform Act of 1996 ( 7 U.S.C. 7333 ) is amended\u2014\n**(1)**\nin subsection (a)(1)(C)\u2014\n**(A)**\nin the matter preceding clause (i), by inserting best facilitates after assistance program that ;\n**(B)**\nin clause (i)\u2014\n**(i)**\nby striking best facilitates the use of that and inserting the use of those ; and\n**(ii)**\nby striking and at the end;\n**(C)**\nin clause (ii)\u2014\n**(i)**\nby striking ensures the availability of that and inserting the public availability of those ; and\n**(ii)**\nby striking the period at the end and inserting a semicolon; and\n**(D)**\nby adding at the end the following:\n(iii) the expansion of crops listed on the national crop table of the Agency with a local average market price; (iv) the voluntary graduation of program participants to the whole farm risk management insurance plan developed under section 522(c)(7) of the Federal Crop Insurance Act ( 7 U.S.C. 1522(c)(7) ); and (v) the establishment of pilot projects for purposes of addressing emerging needs of producers and collecting data to support the development of policies or plans of insurance offered under the Federal Crop Insurance Act ( 7 U.S.C. 1501 et seq. ). ;\n**(2)**\nin subsection (b), by striking paragraph (4) and inserting the following:\n(4) Streamlined application process (A) Definition of whole farm plan In this paragraph, the term whole farm plan means the whole farm risk management insurance plan developed under section 522(c)(7) of the Federal Crop Insurance Act ( 7 U.S.C. 1522(c)(7) ). (B) Establishment (i) In general The Secretary shall establish a streamlined process for the submission of records and acreage reports under paragraphs (2) and (3), respectively, for\u2014 (I) diverse production systems, such as those typical of urban production systems; (II) other small-scale production systems; and (III) direct-to-consumer production systems. (ii) Inclusions The streamlined process established under clause (i) shall include\u2014 (I) reduced acreage report requirements; and (II) allowing the submission to the Secretary of 2 reports per year so as to accommodate later acreage reporting. (C) Revenue-based option (i) Establishment Notwithstanding paragraphs (2) and (3) or subsection (a)(1)(A), the Secretary shall establish a streamlined revenue-based coverage option that is available, on a voluntary basis, to any producer eligible for assistance under this section. (ii) Submission of historical revenue The Secretary shall accept the Internal Revenue Service Tax Form Schedule F, or successor forms, as sufficient for the establishment of historical adjusted revenue, subject to the condition that approved insurance providers may request additional verifiable records in cases where there is documented evidence, made clear to the applicant, that farm tax records are incomplete. (D) On-ramp to whole farm plan (i) In general In the case of a producer using diverse production systems described in subparagraph (B)(i) that may be eligible for the whole farm plan, the Secretary, acting through the Administrator of the Agency, shall establish a streamlined revenue-based option under the noninsured crop disaster assistance program under this section to assist the producer to transition, on a voluntary basis, from the noninsured crop disaster assistance program under this section to the whole farm plan. The Secretary may provide for such other options as may be necessary to assist producers with such a transition who are unable to purchase a whole farm plan. (ii) Requirements The streamlined revenue-based option established under clause (i) shall offer a premium discount of\u2014 (I) 25 percent for the first crop year for which a producer\u2014 (aa) certifies that the producer will transition from the noninsured crop disaster assistance program under this section to the whole farm plan not later than 3 years after the date of the certification; and (bb) provides revenue history with respect to that crop year; (II) 50 percent for the crop year following the crop year described in subclause (I) if the producer\u2014 (aa) certifies that the producer will transition from the noninsured crop disaster assistance program under this section to the whole farm plan not later than 2 years after the date of the certification; and (bb) provides revenue history with respect to that crop year; and (III) 50 percent for the crop year following the crop year described in subclause (II) if the producer\u2014 (aa) purchases insurance under the whole farm plan not later than 1 year after the date of the certification; and (bb) provides revenue history with respect to that crop year. (iii) Tax Form Schedule F The Secretary shall accept the Internal Revenue Service Tax Form Schedule F (or a successor form) with respect to a producer for purposes of establishing revenue history under clause (ii). (iv) Revenue history sharing The Secretary shall submit to the Federal Crop Insurance Corporation the revenue history submitted to the Secretary pursuant to clause (ii). (E) Rulemaking Not later than 90 days after the date of the enactment of the Save Our Small Farms Act of 2025 , the Secretary shall issue regulations to ensure that premium discounts under this paragraph are only available to producers who transition to a whole farm plan, as described in subparagraph (D)(i). ;\n**(3)**\nin subsection (c), by adding at the end the following:\n(5) Notice of certain losses Notwithstanding any other provision of law (including regulations), a producer of a hand-harvested or rapidly deteriorating crop may submit to the Secretary notification of a loss of that crop 120 hours or more after the loss in order to be eligible for assistance under this section. (6) Appraisal of loss (A) In general In any case in which an appraisal of crop acreage is requested by a producer or determined to be necessary by the Secretary for a year in which a notice of loss is filed under this subsection, particularly in any case in which a loss adjuster is not available within 72 hours of the notice, the Secretary shall permit the following alternatives to an in-person appraisal by a loss adjuster: (i) Remote appraisal, including time-stamped photographs, drone footage, and other technology applications. (ii) Appraisal by field office staff of the Agency with requisite training, in conjunction with a remote appraisal under clause (i). (B) Training The Secretary shall require field office staff to attend noninsured crop disaster assistance appraisal training for purposes of subparagraph (A)(ii). ;\n**(4)**\nin subsection (e)(3), by striking 65 percent and inserting 100 percent ;\n**(5)**\nin subsection (i)(2)\u2014\n**(A)**\nin subparagraph (A), by striking and at the end;\n**(B)**\nin subparagraph (B), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(C) notwithstanding subparagraphs (A) and (B), in the case of a limited resource, beginning, or socially disadvantaged farmer, as determined by the Secretary, a veteran farmer or rancher (as defined in section 2501(a) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279(a) )), or a producer participating in the streamlined revenue-based option pursuant to subsection (b)(4)(C), $600,000. ;\n**(6)**\nin subsection (k)(2)\u2014\n**(A)**\nby striking defined by the Secretary, or a veteran and inserting determined by the Secretary, a veteran ; and\n**(B)**\nby inserting , or a producer participating in the streamlined revenue-based option pursuant to subsection (b)(4)(C) before the period at the end;\n**(7)**\nin subsection (l), by striking paragraph (3) and inserting the following:\n(3) Premium discount The coverage made available under this subsection shall be available to limited resource, beginning, or socially disadvantaged farmers, as determined by the Secretary, veteran farmers or ranchers (as defined in section 2501(a) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279(a) )), and producers participating in the streamlined revenue-based option pursuant to subsection (b)(4)(C), in exchange for a premium that is 25 percent of the premium determined under paragraph (2). ; and\n**(8)**\nby adding at the end the following:\n(m) Delivery The Secretary shall collaborate with outreach and technical assistance providers, extension offices, and State departments of agriculture to advertise the noninsured crop disaster assistance program under this section, particularly to limited resource, beginning, or socially disadvantaged farmers, as determined by the Secretary, veteran farmers or ranchers (as defined in section 2501(a) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279(a) )), and producers eligible to participate in the streamlined revenue-based option pursuant to subsection (b)(4)(C). .\n#### 3. Whole farm revenue protection\nSection 522(c) of the Federal Crop Insurance Act ( 7 U.S.C. 1522(c) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (B), by striking and at the end;\n**(B)**\nin subparagraph (C), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(D) increase participation by producers\u2014 (i) marketing direct-to-consumers; (ii) marketing through intermediated sales in local and regional markets; (iii) using farm identity-preserved marketing; or (iv) undertaking producer education on how to use direct market prices. ;\n**(2)**\nin paragraph (7)\u2014\n**(A)**\nin subparagraph (A), by striking , with a liability limitation of $1,500,000, ;\n**(B)**\nin subparagraph (B), by inserting or in combination with after in lieu of ;\n**(C)**\nin subparagraph (C)\u2014\n**(i)**\nin the matter preceding clause (i), by striking may and inserting shall ;\n**(ii)**\nin clause (i), by striking or at the end;\n**(iii)**\nby redesignating clause (ii) as clause (iii); and\n**(iv)**\nby inserting after clause (i) the following:\n(ii) utilize a resource-conserving crop rotation (as defined in section 1240L(d)(1) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u201324(d)(1) )); or ;\n**(D)**\nin subparagraph (D), by striking may and inserting shall ;\n**(E)**\nin subparagraph (E)\u2014\n**(i)**\nin clause (i), in the matter preceding subclause (I), by striking 18 months after the date of enactment of the Agriculture Improvement Act of 2018 and inserting 1 year after the date of the enactment of the Save Our Small Farms Act of 2025 ;\n**(ii)**\nin clause (ii), in the matter preceding subclause (I), by striking subclause and inserting clause ; and\n**(iii)**\nby adding at the end the following:\n(iii) Additional review Not later than 1 year after the date of the enactment of the Save Our Small Farms Act of 2025 , and annually thereafter, the Corporation shall\u2014 (I) review any limitations on insurable revenue (including the overall limitation and limitations specific to animals, animal products, greenhouse and nursery, and aquaculture) to ensure the limitations are adequate to cover the financial risks associated with the production of high-value agricultural products; and (II) submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report that includes a summary of the most recent review conducted under subclause (I) and any expected changes to the policy for the following reinsurance year. (iv) Public report Not later than 18 months after the date of the enactment of the Save Our Small Farms Act of 2025 , the Board shall make publicly available a report describing the decisions made by the Board with respect to each factor described in clause (ii). ;\n**(F)**\nby redesignating subparagraph (F) as subparagraph (G); and\n**(G)**\nby inserting after subparagraph (E) the following:\n(F) Modifications to improve effectiveness for specialty crops and diversified farms (i) In general Not later than 18 months after the date of the enactment of the Save Our Small Farms Act of 2025 , the Corporation shall implement the following modifications to the plan developed under subparagraph (A): (I) Establish that appropriate income reported on Internal Revenue Service Tax Form Schedule F (or a successor form), shall be sufficient for the establishment of historical adjusted revenue, subject to the condition that approved insurance providers may request additional verifiable records in cases where there is documented evidence, made clear to the applicant, that farm tax records are incomplete. (II) Presume that declines in total market price are due to unavoidable natural causes, unless the Corporation demonstrates the extent to which the decline in lower market price is the direct result of an uninsured manmade event. (III) Require that any adjustment of the revenue guarantee by an approved insurance provider, after the approved insurance provider accepts a revised farm operation report from the insured, is contingent on approval from the Risk Management Agency, and allow the insured an opportunity to appeal any denial by the Risk Management Agency of that revenue guarantee adjustment to the National Appeals Division. (IV) With respect to whole farm revenue protection policies, raise the limit on growth expansion for all producers to the lower of\u2014 (aa) 100 percent of historic revenue; and (bb) $500,000. (V) In the case of a rejection of an application from a producer for a whole farm insurance plan, the approved insurance provider involved shall notify the producer of such rejection, and include in such notification a written rationale with sufficient detail for the producer to understand any deficiencies in the application and how to cure those deficiencies. (VI) Expand the maximum commodity count eligible for the diversification-based premium discount under subparagraph (C) to apply to 10 commodities produced. The Secretary may raise that maximum commodity count eligible for the diversification-based premium discount to include more than 10 commodities if determined necessary. (VII) Moderate the impact of disaster years, as determined by the Secretary, on historic revenue by\u2014 (aa) counting indemnities as historic revenue for loss years, including payments made under the noninsured crop disaster assistance program established by section 196 of the Federal Agriculture Improvement and Reform Act of 1996 ( 7 U.S.C. 7333 ); or (bb) using an assigned yield floor similar to the limitation described in section 508(g)(6)(A)(i), as determined by the Secretary. (VIII) Allow prices and yields used to establish coverage in other Federal crop insurance policies to be used as prices and yields for whole farm revenue protection policies. (IX) Establish a process for records and acreage reports submitted by producers for the noninsured crop disaster assistance program established by section 196 of the Federal Agriculture Improvement and Reform Act of 1996 ( 7 U.S.C. 7333 ) to be accepted as documentation for the requisite actual production history for whole farm revenue protection policies. (X) Increase agent incentives to market whole farm revenue protection by\u2014 (aa) providing annual additional administrative and operating subsidies, at a rate determined by the Secretary, to approved insurance providers for any new whole farm revenue policies written in a given year; and (bb) with respect to a whole farm revenue protection policy, requiring approved insurance providers to pay to the agent who sold that policy an amount equal to the total administrative and operating subsidy earned on that policy. (XI) Require approved insurance providers to accept or reject applications, by written decision, within 75 days of receipt of the application, with failure resulting in a reduction by 15 percent of the amount of the administrative and operating subsidy that the approved insurance provider receives from the Corporation for that policy. (ii) Administrative improvements Not later than 18 months after the date of the enactment of the Save Our Small Farms Act of 2025 , for purposes of improving the plan developed under subparagraph (A), the Corporation shall carry out the following activities: (I) Create and maintain a web-accessible tool for producers to locate agents experienced in selling a whole farm revenue protection policy. (II) Provide additional educational and training opportunities to approved insurance providers and insurance agents, which may include entering into agreements with 1 or more entities\u2014 (aa) to provide technical assistance to interested producers; (bb) to conduct education and outreach to agents and insurance providers; and (cc) to develop best practices for underwriting. (III) Conduct a pilot program to create a pricing library for agents and insurance providers, also accessible to the public and entities that provide technical assistance to farmers using data from\u2014 (aa) the Agricultural Marketing Service; (bb) the noninsured crop disaster assistance program established by section 196 of the Federal Agriculture Improvement and Reform Act of 1996 ( 7 U.S.C. 7333 ); (cc) approved policies of the Board; (dd) land-grant colleges or universities and other institutions of higher education; (ee) grower boards or commissions; and (ff) other relevant sources, as determined by the Secretary. (iii) Availability of pricing library The Risk Management Agency may, as determined by the Secretary, offer the pricing library described in item (aa) to agents and insurance providers in connection with policies other than policies developed under subparagraph (A). (iv) Public report Not later than 18 months after the date of the enactment of the Save Our Small Farms Act of 2025 , the Board shall make publicly available a report describing the decisions made by the Board with respect to each modification described in clauses (i) and (ii). ; and\n**(3)**\nin paragraph (18), by adding at the end the following:\n(D) Continuation of plan The Administrator of the Risk Management Agency shall continue to offer the micro farm insurance plan offered pursuant to subparagraph (A)(ii) in all States and counties of the United States. (E) Modifications to improve effectiveness for micro farms Not later than 180 days after the date of the enactment of the Save Our Small Farms Act of 2025 , the Corporation shall implement the following modifications to the micro farm insurance plan offered pursuant to subparagraph (A)(ii): (i) Allow vertically integrated operations to access coverage under a micro farm policy. (ii) Allow producers with a micro farm policy to also purchase crop-specific Federal crop insurance policies for crops insured under the micro farm policy. (iii) Expand the maximum approved revenue to establish eligibility for a micro farm plan of insurance to $1,000,000 or more, as determined by the Secretary. .\n#### 4. Single index insurance policy\n##### (a) In general\nSection 522(c) of the Federal Crop Insurance Act ( 7 U.S.C. 1522(c) ), as amended by section 3, is further amended by adding at the end the following:\n(20) Single index insurance policy (A) Definitions In this paragraph: (i) Covered crop or commodity The term covered crop or commodity means any crop or commodity (including a specialty crop) on a farm except timber, forest products, animals for sport or show, and pets. (ii) Covered policy The term covered policy means the single index insurance policy described in subparagraph (B)(i). (iii) Covered weather condition (I) In general The term covered weather condition means any of the following weather conditions that are found to be closely correlated with agricultural income losses: (aa) High winds. (bb) Excessive moisture and flooding. (cc) Extreme heat. (dd) Abnormal freeze conditions. (ee) Wildfire. (ff) Hail. (gg) Drought. (hh) Any other severe weather or growing conditions applicable to small-scale farmers, as determined by the Secretary. (II) Data The existence of a weather condition described in subclause (I) shall be determined by indices that prioritize using data from the National Oceanic and Atmospheric Administration, as available, but may use other federally or State certified weather data sources, public and private satellite data, and weather and climate data and models, if necessary, as determined by the Secretary. (B) Policy (i) In general The Corporation shall carry out research and development, or offer to enter into 1 or more contracts with 1 or more qualified persons to carry out research and development, to develop a single index policy to insure against agricultural income losses due to 1 or more covered weather conditions. (ii) Coverage Research and development on the covered policy under clause (i) shall require that coverage is available in all 50 States (including Indian Tribes), the District of Columbia, American Samoa, Guam, the Commonwealth of the Northern Mariana Islands, the Commonwealth of Puerto Rico, and the Virgin Islands of the United States. (iii) Option to buy-up or buy-down (I) In general Research and development on the covered policy under clause (i) shall consider permitting a holder of the covered policy to elect to buy-up to 150 percent, subject to subclause (II), or buy-down to 5 percent, of the median county-level adjusted gross income for farms, in 5-percent increments, to reflect the income of the individual farm business of the holder insured under the covered policy. (II) Limitation A holder of a covered policy may buy-up under subclause (I) only if the farms of the holder insured under the covered policy have at least 3 covered crops or commodities. (iv) Priority features of policy In carrying out research and development on the covered policy under clause (i), the following features may be given priority: (I) Agricultural income losses under the covered policy include\u2014 (aa) losses for all covered crops or commodities; and (bb) losses to the value of packing, packaging, or any other similar on-farm activity that the Corporation determines necessary to remove a covered crop or commodity from the field. (II) Payments are made under the covered policy not later than 30 days after the occurrence of a covered weather condition in the county in which the applicable farm of the farmer is located or an adjacent county. (III) Provision of seasonal coverage periods. (IV) Provision of special consideration to concerns facing individual farm businesses\u2014 (aa) that have less than $350,000 in adjusted gross income; and (bb) with respect to which a farmer is an underserved producer (as defined in section 508(a)(7)(A)). (V) Paperwork requirements are reduced for farmers seeking to obtain a covered policy. (v) Consultation In carrying out research and development on the covered policy under clause (i), the Corporation\u2014 (I) shall hold stakeholder meetings to solicit producer and agent feedback; and (II) may consult with licensed actuaries with experience developing index policies insuring agricultural production. (C) Report Not later than 1 year after the date of the enactment of this paragraph, the Corporation shall make publicly available a report that describes\u2014 (i) the results of the research and development carried out under this paragraph; and (ii) recommendations to Congress with respect to those results, including\u2014 (I) any challenges to developing the covered policy; and (II) options to address those challenges. .\n##### (b) Technical amendment\nSection 531(a)(18) of the Federal Crop Insurance Act ( 7 U.S.C. 1531(a)(18) ) is amended by striking section 2501(e) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279(e) ) and inserting section 2501(a) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279(a) ). .",
      "versionDate": "2025-03-27",
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
        "actionDate": "2025-01-23",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "231",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "WEATHER Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-06T17:19:25Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2435ih.xml"
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
      "title": "Save Our Small Farms Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-05T09:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Save Our Small Farms Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-05T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Agriculture Improvement and Reform Act of 1996 to assist farmers relying on the noninsured crop disaster assistance program by lowering the cost of purchasing coverage, reducing paperwork burdens, and increasing payouts under that program, and to incentivize farmers to transition gradually to a comprehensive insurance policy under the whole farm risk management insurance plan by offering progressive premium discounts on a commitment to purchase a whole farm plan of insurance.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-05T09:18:23Z"
    }
  ]
}
```
