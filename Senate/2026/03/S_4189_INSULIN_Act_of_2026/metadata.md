# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4189?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4189
- Title: INSULIN Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4189
- Origin chamber: Senate
- Introduced date: 2026-03-25
- Update date: 2026-05-20T11:03:29Z
- Update date including text: 2026-05-20T11:03:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in Senate
- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-03-25: Introduced in Senate

## Actions

- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4189",
    "number": "4189",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "INSULIN Act of 2026",
    "type": "S",
    "updateDate": "2026-05-20T11:03:29Z",
    "updateDateIncludingText": "2026-05-20T11:03:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-25",
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
          "date": "2026-03-25T17:17:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "ME"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "LA"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NV"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "AL"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-03-25",
      "state": "ME"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "AK"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "AZ"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "IA"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "WI"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "AL"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "DE"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "MS"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "VA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-05-18",
      "state": "WV"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "DE"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4189is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4189\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2026 Mrs. Shaheen (for herself, Ms. Collins , Mr. Warnock , Mr. Kennedy , Ms. Rosen , Mr. Tuberville , Mr. King , Ms. Murkowski , Mr. Kelly , Mr. Grassley , Ms. Baldwin , and Mrs. Britt ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo reduce the price of insulin and provide for patient protections with respect to the cost of insulin.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Improving Needed Safeguards for Users of Lifesaving Insulin Now Act of 2026 or the INSULIN Act of 2026 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Sense of Congress.\nTITLE I\u2014Commercial market patient protections\nSec. 101. Requirements with respect to cost-sharing for certain insulin products.\nSec. 102. Application to retiree and certain small group plans.\nSec. 103. Administration.\nTITLE II\u2014Pharmacy benefit manager transparency and rebate reform\nSec. 201. Full rebate on insulin pass-through to plan.\nTITLE III\u2014Biosimilar biological product and generic drug competition and affordability\nSec. 301. Ensuring timely access to generics.\nSec. 302. Expediting competitive biosimilar competition.\nSec. 303. Insulin competition report.\nTITLE IV\u2014Programs for providing affordable insulin to uninsured individuals\nSec. 401. Pilot program for providing affordable insulin to uninsured individuals.\nSec. 402. GAO study on uninsured individuals who use insulin.\nSec. 403. Insulin resource center and hotline for uninsured individuals.\n#### 2. Sense of Congress\nIt is the sense of Congress that Congress should enact subsequent legislation that provides for an offset for any costs to the Federal Government resulting from the enactment of this Act.\nI\nCommercial market patient protections\n#### 101. Requirements with respect to cost-sharing for certain insulin products\n##### (a) In general\nPart D of title XXVII of the Public Health Service Act ( 42 U.S.C. 300gg\u2013111 et seq. ) is amended by adding at the end the following:\n2799A\u201312. Requirements with respect to cost-sharing for certain insulin products (a) In general For plan years beginning on or after January 1, 2027, a group health plan or health insurance issuer offering group or individual health insurance coverage shall provide coverage of selected insulin products, and with respect to such products, shall not\u2014 (1) apply any deductible; or (2) impose any cost-sharing requirements in excess of, per 30-day supply\u2014 (A) for any applicable plan year beginning before January 1, 2028, $35; or (B) for any plan year beginning on or after January 1, 2028, the lesser of\u2014 (i) $35; or (ii) the amount equal to 25 percent of the negotiated price of the selected insulin product net of all price concessions received by or on behalf of the plan or issuer, including price concessions received by or on behalf of third-party entities providing services to the plan or issuer, such as pharmacy benefit management services or third party administrators. (b) Definitions In this section: (1) Selected insulin products The term selected insulin products means, for any plan year beginning on or after January 1, 2027, at least one of each dosage form (such as vial, pen, or inhaler dosage forms) of each different type (such as rapid-acting, short-acting, intermediate-acting, long-acting, and pre-mixed) of insulin, when such form is licensed and marketed, as selected by the group health plan or health insurance issuer. (2) Insulin The term insulin means insulin that is licensed under subsection (a) or (k) of section 351 and continues to be marketed pursuant to such licensure. (c) Out-of-Network providers Nothing in this section requires a plan or issuer that has a network of providers to provide benefits for selected insulin products described in this section that are delivered by an out-of-network provider, or precludes a plan or issuer that has a network of providers from imposing higher cost-sharing than the levels specified in subsection (a) for selected insulin products described in this section that are delivered by an out-of-network provider. (d) Rule of construction Subsection (a) shall not be construed to require coverage of, or prevent a group health plan or health insurance issuer from imposing cost-sharing other than the levels specified in subsection (a) on, insulin products that are not selected insulin products, to the extent that such coverage is not otherwise required and such cost-sharing is otherwise permitted under Federal and applicable State law. (e) Application of cost-Sharing towards deductibles and out-of-Pocket maximums Any cost-sharing payments made pursuant to subsection (a)(2) shall be counted toward any deductible or out-of-pocket maximum that applies under the plan or coverage. (f) Other requirements A group health plan or health insurance issuer offering group or individual health insurance coverage shall not impose, directly or through an entity providing pharmacy benefit management services, any prior authorization or other medical management requirement, or other similar conditions, on selected insulin products, except as clinically justified for safety reasons, to ensure reasonable quantity limits and as specified by the Secretary. .\n##### (b) No effect on other cost-Sharing\nSection 1302(d)(2) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18022(d)(2) ) is amended by adding at the end the following new subparagraph:\n(D) Special rule relating to insulin coverage For plans years beginning on or after January 1, 2028, the exemption of coverage of selected insulin products (as defined in section 2799A\u201312(b) of the Public Health Service Act) from the application of any deductible pursuant to section 2799A\u201312(a)(1) of such Act, section 727(a)(1) of the Employee Retirement Income Security Act of 1974, or section 9827(a)(1) of the Internal Revenue Code of 1986 shall not be considered when determining the actuarial value of a qualified health plan under this subsection. .\n##### (c) Coverage of certain insulin products under catastrophic plans\nSection 1302(e) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18022(e) ) is amended by adding at the end the following:\n(4) Coverage of certain insulin products (A) In general Notwithstanding paragraph (1)(B)(i), for plan years beginning on or after January 1, 2027, a health plan described in paragraph (1) shall provide coverage of selected insulin products, in accordance with section 2799A\u201312 of the Public Health Service Act, before an enrolled individual has incurred, during the plan year, cost-sharing expenses in an amount equal to the annual limitation in effect under subsection (c)(1) for the plan year. (B) Terminology For purposes of subparagraph (A)\u2014 (i) the term selected insulin products has the meaning given such term in section 2799A\u201312(b) of the Public Health Service Act; and (ii) the requirements of section 2799A\u201312 of such Act shall be applied by deeming each reference in such section to individual health insurance coverage to be a reference to a plan described in paragraph (1). .\n##### (d) ERISA\n**(1) In general**\nSubpart B of part 7 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1185 et seq. ) is amended by adding at the end the following:\n727. Requirements with respect to cost-sharing for certain insulin products (a) In general For plan years beginning on or after January 1, 2027, a group health plan or health insurance issuer offering group health insurance coverage shall provide coverage of selected insulin products, and with respect to such products, shall not\u2014 (1) apply any deductible; or (2) impose any cost-sharing requirements in excess of, per 30-day supply\u2014 (A) for any applicable plan year beginning before January 1, 2028, $35; or (B) for any plan year beginning on or after January 1, 2028, the lesser of\u2014 (i) $35; or (ii) the amount equal to 25 percent of the negotiated price of the selected insulin product net of all price concessions received by or on behalf of the plan or issuer, including price concessions received by or on behalf of third-party entities providing services to the plan or issuer, such as pharmacy benefit management services or third party administrators. (b) Definitions In this section: (1) Selected insulin products The term selected insulin products means, for any plan year beginning on or after January 1, 2027, at least one of each dosage form (such as vial, pen, or inhaler dosage forms) of each different type (such as rapid-acting, short-acting, intermediate-acting, long-acting, and pre-mixed) of insulin, when such form is licensed and marketed, as selected by the group health plan or health insurance issuer. (2) Insulin The term insulin means insulin that is licensed under subsection (a) or (k) of section 351 of the Public Health Service Act ( 42 U.S.C. 262 ) and continues to be marketed pursuant to such licensure. (c) Out-of-Network providers Nothing in this section requires a plan or issuer that has a network of providers to provide benefits for selected insulin products described in this section that are delivered by an out-of-network provider, or precludes a plan or issuer that has a network of providers from imposing higher cost-sharing than the levels specified in subsection (a) for selected insulin products described in this section that are delivered by an out-of-network provider. (d) Rule of construction Subsection (a) shall not be construed to require coverage of, or prevent a group health plan or health insurance issuer from imposing cost-sharing other than the levels specified in subsection (a) on, insulin products that are not selected insulin products, to the extent that such coverage is not otherwise required and such cost-sharing is otherwise permitted under Federal and applicable State law. (e) Application of cost-Sharing towards deductibles and out-of-Pocket maximums Any cost-sharing payments made pursuant to subsection (a)(2) shall be counted toward any deductible or out-of-pocket maximum that applies under the plan or coverage. (f) Other requirements A group health plan or health insurance issuer offering group health insurance coverage shall not impose, directly or through an entity providing pharmacy benefit management services, any prior authorization or other medical management requirement, or other similar conditions, on selected insulin products, except as clinically justified for safety reasons, to ensure reasonable quantity limits and as specified by the Secretary. .\n**(2) Clerical amendment**\nThe table of contents in section 1 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1001 et seq. ) is amended by inserting after the item relating to section 726 the following:\nSec. 727. Requirements with respect to cost-sharing for certain insulin products. .\n##### (e) Internal Revenue Code\n**(1) In general**\nSubchapter B of chapter 100 of the Internal Revenue Code of 1986 is amended by adding at the end the following:\n9827. Requirements with respect to cost-sharing for certain insulin products (a) In general For plan years beginning on or after January 1, 2027, a group health plan shall provide coverage of selected insulin products, and with respect to such products, shall not\u2014 (1) apply any deductible; or (2) impose any cost-sharing requirements in excess of, per 30-day supply\u2014 (A) for any applicable plan year beginning before January 1, 2028, $35; or (B) for any plan year beginning on or after January 1, 2028, the lesser of\u2014 (i) $35; or (ii) the amount equal to 25 percent of the negotiated price of the selected insulin product net of all price concessions received by or on behalf of the plan, including price concessions received by or on behalf of third-party entities providing services to the plan, such as pharmacy benefit management services or third party administrators. (b) Definitions In this section: (1) Selected insulin products The term selected insulin products means, for any plan year beginning on or after January 1, 2027, at least one of each dosage form (such as vial, pen, or inhaler dosage forms) of each different type (such as rapid-acting, short-acting, intermediate-acting, long-acting, and pre-mixed) of insulin, when such form is licensed and marketed, as selected by the group health plan. (2) Insulin The term insulin means insulin that is licensed under subsection (a) or (k) of section 351 of the Public Health Service Act ( 42 U.S.C. 262 ) and continues to be marketed pursuant to such licensure. (c) Out-of-Network providers Nothing in this section requires a plan that has a network of providers to provide benefits for selected insulin products described in this section that are delivered by an out-of-network provider, or precludes a plan that has a network of providers from imposing higher cost-sharing than the levels specified in subsection (a) for selected insulin products described in this section that are delivered by an out-of-network provider. (d) Rule of construction Subsection (a) shall not be construed to require coverage of, or prevent a group health plan from imposing cost-sharing other than the levels specified in subsection (a) on, insulin products that are not selected insulin products, to the extent that such coverage is not otherwise required and such cost-sharing is otherwise permitted under Federal and applicable State law. (e) Application of cost-Sharing towards deductibles and out-of-Pocket maximums Any cost-sharing payments made pursuant to subsection (a)(2) shall be counted toward any deductible or out-of-pocket maximum that applies under the plan. (f) Other requirements A group health plan shall not impose, directly or through an entity providing pharmacy benefit management services, any prior authorization or other medical management requirement, or other similar conditions, on selected insulin products, except as clinically justified for safety reasons, to ensure reasonable quantity limits and as specified by the Secretary. .\n**(2) Clerical amendment**\nThe table of sections for subchapter B of chapter 100 of such Code is amended by adding at the end the following new item:\nSec. 9827. Requirements with respect to cost-sharing for certain insulin products. .\n#### 102. Application to retiree and certain small group plans\n##### (a) ERISA\nSection 732(a) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1191a(a) ) is amended by striking section 711 and inserting sections 711 and 727 .\n##### (b) IRC\nThe Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin section 9831(a), by adding at the end the following flush text:\nParagraph (2) shall not apply to the requirements under sections 9811 and 9827. ; and\n**(2)**\nin section 4980D(d)(1), by striking section 9811 and inserting section 9811 or 9827 .\n#### 103. Administration\n##### (a) Implementation\nNotwithstanding any other provision of law, the Secretary of Health and Human Services, the Secretary of Labor, and the Secretary of the Treasury may implement the provisions of, including the amendments made by, this title for plan years that begin on or after January 1, 2027, and end not later than January 1, 2030, by subregulatory guidance, program instruction, or otherwise.\n##### (b) Non-Application of the Paperwork Reduction Act\nChapter 35 of title 44, United States Code (commonly referred to as the Paperwork Reduction Act of 1995 ), shall not apply to the provisions of, including the amendments made by, this title.\nII\nPharmacy benefit manager transparency and rebate reform\n#### 201. Full rebate on insulin pass-through to plan\n##### (a) PHSA\nPart D of title XXVII of the Public Health Service Act ( 42 U.S.C. 300gg\u2013111 et seq. ), as amended by section 101, is further amended by adding at the end the following:\n2799A\u201313. Full rebate on insulin pass-through to plan (a) In general A pharmacy benefits manager, a third-party administrator of a group health plan, a health insurance issuer offering group health insurance coverage, or an entity providing pharmacy benefits management services under such health plan or health insurance coverage shall remit 100 percent of rebates, fees, alternative discounts, and all other remuneration received from a pharmaceutical manufacturer, distributor or any other third party, that are related to utilization of insulin under such health plan or health insurance coverage, to the group health plan. (b) Form and manner of remittance Such rebates, fees, alternative discounts, and other remuneration shall be\u2014 (1) remitted to the group health plan in a timely fashion after the period for which such rebates, fees, or other remuneration is calculated, and in no case later than 90 days after the end of such period; (2) fully disclosed and enumerated to the group health plan sponsor; and (3) available for audit by the plan sponsor, or a third-party designated by a plan sponsor no less than once per plan year. .\n##### (b) ERISA\n**(1) In general**\nSubpart B of part 7 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1185 et seq. ), as amended by section 101, is further amended by adding at the end the following:\n728. Full rebate on insulin pass-through to plan (a) In general A pharmacy benefits manager, a third-party administrator of a group health plan, a health insurance issuer offering group health insurance coverage, or an entity providing pharmacy benefits management services under such health plan or health insurance coverage shall remit 100 percent of rebates, fees, alternative discounts, and all other remuneration received from a pharmaceutical manufacturer, distributor or any other third party, that are related to utilization of insulin under such health plan or health insurance coverage, to the group health plan. (b) Form and manner of remittance Such rebates, fees, alternative discounts, and other remuneration shall be\u2014 (1) remitted to the group health plan in a timely fashion after the period for which such rebates, fees, or other remuneration is calculated, and in no case later than 90 days after the end of such period; (2) fully disclosed and enumerated to the group health plan sponsor; and (3) available for audit by the plan sponsor, or a third-party designated by a plan sponsor no less than once per plan year. .\n**(2) Clerical amendment**\nThe table of contents in section 1 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1001 et seq. ), as amended by section 101, is further amended by inserting after the item relating to section 727 the following:\nSec. 728. Full rebate on insulin pass-through to plan. .\n##### (c) Internal Revenue Code\n**(1) In general**\nSubchapter B of chapter 100 of the Internal Revenue Code of 1986, as amended by section 101, is further amended by adding at the end the following new section:\n9828. Full rebate on insulin pass-through to plan (a) In general A pharmacy benefits manager, a third-party administrator of a group health plan, or an entity providing pharmacy benefits management services under such health plan shall remit 100 percent of rebates, fees, alternative discounts, and all other remuneration received from a pharmaceutical manufacturer, distributor or any other third party, that are related to utilization of insulin under such health plan, to the group health plan. (b) Form and manner of remittance Such rebates, fees, alternative discounts, and other remuneration shall be\u2014 (1) remitted to the group health plan in a timely fashion after the period for which such rebates, fees, or other remuneration is calculated, and in no case later than 90 days after the end of such period; (2) fully disclosed and enumerated to the group health plan sponsor; and (3) available for audit by the plan sponsor, or a third-party designated by a plan sponsor no less than once per plan year. .\n**(2) Clerical amendment**\nThe table of sections for subchapter B of chapter 100 of such Code, as amended by section 101, is further amended by adding at the end the following new item:\nSec. 9828. Full rebate on insulin pass-through to plan. .\nIII\nBiosimilar biological product and generic drug competition and affordability\n#### 301. Ensuring timely access to generics\nSection 505(q) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(q) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A)(i), by inserting , 10.31, after 10.30 ;\n**(B)**\nin subparagraph (E)\u2014\n**(i)**\nby striking application and and inserting application or ;\n**(ii)**\nby striking If the Secretary and inserting the following:\n(i) In general If the Secretary ; and\n**(iii)**\nby striking the second sentence and inserting the following:\n(ii) Primary purpose of delaying (I) In general In determining whether a petition was submitted with the primary purpose of delaying an application, the Secretary may consider the following factors: (aa) Whether the petition was submitted in accordance with paragraph (2)(B), based on when the petitioner knew or reasonably should have known the relevant information relied upon to form the basis of such petition. (bb) Whether the petitioner has submitted multiple or serial petitions or supplements to petitions raising issues that reasonably could have been known to the petitioner at the time of submission of the earlier petition or petitions. (cc) Whether the petition was submitted close in time to a known, first date upon which an application under subsection (b)(2) or (j) of this section or section 351(k) of the Public Health Service Act could be approved. (dd) Whether the petition was submitted without relevant data or information in support of the scientific positions forming the basis of such petition. (ee) Whether the petition raises the same or substantially similar issues as a prior petition to which the Secretary has responded substantively already, including if the subsequent submission follows such response from the Secretary closely in time. (ff) Whether the petition requests changing the applicable standards that other applicants are required to meet, including requesting testing, data, or labeling standards that are more onerous or rigorous than the standards the Secretary has determined to be applicable to the listed drug, reference product, or petitioner\u2019s version of the same drug. (gg) The petitioner's record of submitting petitions to the Food and Drug Administration that have been determined by the Secretary to have been submitted with the primary purpose of delay. (hh) Other relevant and appropriate factors, which the Secretary shall describe in guidance. (II) Guidance The Secretary may issue or update guidance, as appropriate, to describe factors the Secretary considers in accordance with subclause (I). ;\n**(C)**\nby adding at the end the following:\n(iii) Referral to the Federal Trade Commission The Secretary shall establish procedures for referring to the Federal Trade Commission any petition or supplement to a petition that the Secretary determines was submitted with the primary purpose of delaying approval of an application. Such procedures shall include notification to the petitioner by the Secretary. ;\n**(D)**\nby striking subparagraph (F);\n**(E)**\nby redesignating subparagraphs (G) through (I) as subparagraphs (F) through (H), respectively; and\n**(F)**\nin subparagraph (H), as so redesignated, by striking submission of this petition and inserting submission of this document ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby redesignating subparagraphs (A) through (C) as subparagraphs (C) through (E), respectively;\n**(B)**\nby inserting before subparagraph (C), as so redesignated, the following:\n(A) In general A person shall submit a petition to the Secretary under paragraph (1) before filing a civil action in which the person seeks to set aside, delay, rescind, withdraw, or prevent submission, review, or approval of an application submitted under subsection (b)(2) or (j) of this section or section 351(k) of the Public Health Service Act. Such petition and any supplement to such a petition shall describe all information and arguments that form the basis of the relief requested in any civil action described in the previous sentence. (B) Timely submission of citizen petition A petition and any supplement to a petition shall be submitted within 60 days after the person knew, or reasonably should have known, the information that forms the basis of the request made in the petition or supplement. ;\n**(C)**\nin subparagraph (C), as so redesignated\u2014\n**(i)**\nin the heading, by striking within 150 days ;\n**(ii)**\nin clause (i), by striking during the 150-day period referred to in paragraph (1)(F), ; and\n**(iii)**\nby amending clause (ii) to read as follows:\n(ii) on or after the date that is 151 days after the date of submission of the petition, the Secretary approves or has approved the application that is the subject of the petition without having made such a final decision. ;\n**(D)**\nby amending subparagraph (D), as so redesignated, to read as follows:\n(D) Dismissal of certain civil actions (i) Petition If a person files a civil action against the Secretary in which a person seeks to set aside, delay, rescind, withdraw, or prevent submission, review, or approval of an application submitted under subsection (b)(2) or (j) of this section or section 351(k) of the Public Health Service Act without complying with the requirements of subparagraph (A), the court shall dismiss without prejudice the action for failure to exhaust administrative remedies. (ii) Timeliness If a person files a civil action against the Secretary in which a person seeks to set aside, delay, rescind, withdraw, or prevent submission, review, or approval of an application submitted under subsection (b)(2) or (j) of this section or section 351(k) of the Public Health Service Act without complying with the requirements of subparagraph (B), the court shall dismiss with prejudice the action for failure to timely file a petition. (iii) Final response If a civil action is filed against the Secretary with respect to any issue raised in a petition timely filed under paragraph (1) in which the petitioner requests that the Secretary take any form of action that could, if taken, set aside, delay, rescind, withdraw, or prevent submission, review, or approval of an application submitted under subsection (b)(2) or (j) of this section or section 351(k) of the Public Health Service Act before the Secretary has taken final agency action on the petition within the meaning of subparagraph (C), the court shall dismiss without prejudice the action for failure to exhaust administrative remedies. ; and\n**(E)**\nin clause (iii) of subparagraph (E), as so redesignated, by striking as defined under subparagraph (2)(A) and inserting within the meaning of subparagraph (C) ; and\n**(3)**\nin paragraph (4)\u2014\n**(A)**\nby striking Exceptions and all that follows through This subsection does and inserting Exceptions.\u2014 This subsection does ;\n**(B)**\nby striking subparagraph (B); and\n**(C)**\nby redesignating clauses (i) and (ii) as subparagraphs (A) and (B), respectively, and adjusting the margins accordingly.\n#### 302. Expediting competitive biosimilar competition\n##### (a) In general\nSection 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ) is amended by adding at the end the following:\n(10) Expediting competitive biosimilar competition (A) In general The Secretary may, at the request of the sponsor of an application under this subsection for a biosimilar biological product that is designated as a competitive biosimilar therapy pursuant to subsection (b), expedite the development and review of such application under this subsection. (B) Designation process (i) Request The sponsor of an application under this subsection may request the Secretary to designate the drug as a competitive biosimilar therapy. A request for such designation may be made concurrently with, or at any time prior to, the submission of a biosimilar biological product license application under this subsection. (ii) Criteria A biological product is eligible for designation as a competitive biosimilar therapy under this paragraph if the Secretary determines that there is inadequate biosimilar competition. (iii) Designation Not later than 60 calendar days after the receipt of a request under clause (i), the Secretary may\u2014 (I) determine whether the biosimilar biological product that is the subject of the request meets the criteria described in clause (ii); and (II) if the Secretary finds that such product meets such criteria, designate the biosimilar biological product as a competitive biosimilar therapy. (C) Actions In expediting the development and review of an application under subparagraph (A), the Secretary may, as requested by the applicant, take actions including the following: (i) Hold meetings with the sponsor and the review team throughout the development of the biosimilar biological product prior to submission of the application under this subsection. (ii) Provide timely advice to, and interactive communication with, the sponsor regarding the development of the drug to ensure that the development program to gather the data necessary for approval is as efficient as practicable. (iii) Involve senior managers and experienced review staff, as appropriate, in a collaborative, coordinated review of such application, including with respect to biological product-device combination products and other complex products. (iv) Assign a cross-disciplinary project lead\u2014 (I) to facilitate an efficient review of the development program and application, including manufacturing inspections; and (II) to serve as a scientific liaison between the review team and the applicant. (D) Inspections With respect to an application described in subparagraph (A), in the case of an inspection report that finds approval of such biological product is dependent upon remediation of a facility, if the applicant attests that necessary changes have been made to the facility, the Secretary shall expedite reinspection of such facility, including establishing a set timeline to reinspect the facility or make a determination about the response of the applicant and whether to approve the application. (E) Reporting requirement Not later than 1 year after the date of licensure under this subsection with respect to a biosimilar biological product for which the development and review is expedited under this paragraph, the holder of the license of such biosimilar biological product shall report to the Secretary on whether the biosimilar biological product has been marketed in interstate commerce since the date of such licensure. (F) Inadequate biosimilar competition In this paragraph, the term inadequate biosimilar competition means, with respect to a biological product, there are fewer than 3 licensed biological products on the list published under paragraph (9)(A) (not including biological products on the discontinued section of such list) that are biosimilar biological products with the same reference product. .\n#### 303. Insulin competition report\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Health and Human Services, in collaboration with the Administrator for the Centers for Medicare & Medicaid Services and the Commissioner of Food and Drugs, shall\u2014\n**(1)**\ncomplete a study to determine the extent of, and causes of, delays in getting insulin products to market, and the market dynamics and extent biosimilar biological product development and competition could increase, or is increasing, the number of biological products approved and available to patients, including by examining barriers to\u2014\n**(A)**\nplacement of biosimilar biological products on health insurance formularies;\n**(B)**\nmarket entry of insulin product in the United States, as compared to other highly developed nations; and\n**(C)**\npatient and provider education around biosimilar biological products; and\n**(2)**\nsubmit a report to Congress that describes the results of the study conducted pursuant to paragraph (1) and recommended policy solutions.\nIV\nPrograms for providing affordable insulin to uninsured individuals\n#### 401. Pilot program for providing affordable insulin to uninsured individuals\nPart P of title III of the Public Health Service Act ( 42 U.S.C. 280g et seq. ) is amended by adding at the end the following:\n399V\u20138. Pilot program for providing affordable insulin to uninsured individuals (a) In general The Secretary shall conduct a 5-year pilot program under which the Secretary awards grants to 10 States for purposes of providing affordable insulin to uninsured individuals. (b) Awards The Secretary shall award grants under this section to 10 States that\u2014 (1) submit an application to the Secretary, at such time, in such manner, and containing such information as the Secretary may require; and (2) have high rates of uninsured individuals and individuals diagnosed with diabetes, which may include high rates of newly diagnosed diabetes. (c) Use of funds A State shall use the grant funds received under this section for any of the following purposes: (1) To assist in the purchase or dispensing of insulin, through Federally qualified health centers and retail community pharmacies, for uninsured individuals. (2) To enroll individuals in programs under which drug manufacturers provide financial or medication assistance to low-income individuals, in order to assist such individuals in obtaining insulin. (3) To allow Federally qualified health centers to establish new, or maintain or expand existing, on-site pharmacies owned and operated by the health center that provide low-cost insulin to patients, and to allow retail community pharmacies to provide low-cost insulin to patients. (4) To engage in other activities to assist uninsured individuals in obtaining insulin, as the Secretary determines appropriate. (d) Formula The Secretary shall establish a formula for purposes of determining the grant amount under this section for each State. Such formula shall\u2014 (1) provide for a minimum amount that will be provided to each State; and (2) take into account the rates of individuals with type 1 or type 2, insulin-dependent diabetes and of uninsured individuals in each State for purposes of determining any additional amounts provided to a State. (e) Accountability and Oversight A State receiving a grant under this section shall, not later than 1 year after receiving the grant, submit a report to the Secretary that includes\u2014 (1) a description of the purposes for which the grant funds received by the State were expended in the preceding fiscal year, and the activities of the State under the grant during such year; and (2) the number of individuals served through the grant. (f) Definitions In this section: (1) Affordable The term affordable , with respect to insulin, means that the out-of-pocket cost to the individual for the insulin is not more than $35 per 1-month supply. (2) Federally-qualified health center The term Federally-qualified health center has the meaning given such term in section 1905(l)(2) of the Social Security Act. (3) Insulin The term insulin means insulin that is licensed under subsection (a) or (k) of section 351 and continues to be marketed under such section. (4) Retail community pharmacy The term retail community pharmacy has the meaning given such term in section 1927(k)(10) of the Social Security Act. (5) Uninsured individual The term uninsured individual means an individual who\u2014 (A) is a citizen of the United States or a qualified alien (as defined in section 431(b) of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996); (B) does not qualify for coverage under a Federal health care program (as defined in section 1128B(f) of the Social Security Act), the health program established under chapter 89 of title 5, United States Code, or a group health plan or group health insurance coverage (as defined in section 2791); and (C) is not entitled to a premium assistance tax credit under section 36B of the Internal Revenue Code of 1986. (g) Authorization of appropriations To carry out this section, there is authorized to be appropriated $100,000,000 for fiscal year 2027, to remain available until expended. .\n#### 402. GAO study on uninsured individuals who use insulin\n##### (a) In general\nThe Comptroller General of the United States shall conduct a study, in consultation with patient, clinical, and provider groups and other experts, and not later than 2 years after the date of enactment of this Act, issue a report, on the characteristics of uninsured individuals who use insulin. Such study and report shall, to the extent data is available, include consideration of\u2014\n**(1)**\nany States or regions in which there is a higher prevalence of such individuals;\n**(2)**\nany identifiable potential reasons for uninsured status;\n**(3)**\ndemographic characteristics of such individuals, such as race and ethnicity; and\n**(4)**\nincome level of such individuals.\n##### (b) Definitions\nIn this section, the terms insulin and uninsured individual have the meanings given such terms in section 399V\u20138 of the Public Health Service Act, as added by section 401.\n#### 403. Insulin resource center and hotline for uninsured individuals\n##### (a) In general\nThe Secretary of Health and Human Services (referred to in this section as the Secretary ) shall award a grant to an eligible entity for purposes of\u2014\n**(1)**\nestablishing and maintaining a resource center of assistance programs offered by manufactures or other entities that are available to uninsured individuals seeking affordable insulin; and\n**(2)**\nconducting the public education activities described in subsection (c)(7).\n##### (b) Eligible entities\nTo be eligible to receive the grant under subsection (a), an entity shall\u2014\n**(1)**\nbe a trade, industry, or professional association, community- and consumer-focused nonprofit entity, or other entity, as determined by the Secretary that\u2014\n**(A)**\nis capable of carrying out the duties described in subsection (c);\n**(B)**\nmeets the standards described in subsection (e); and\n**(C)**\nprovides information consistent with the standards developed under subsection (f); and\n**(2)**\nsubmit an application to the Secretary, at such time, in such manner, and containing such information as the Secretary may require, including information demonstrating that the entity\u2014\n**(A)**\nhas existing relationships, or could readily establish relationships, with consumers (including uninsured individuals), health care providers, manufacturers of insulin, social service providers, pharmacies, and other experts that the Secretary determines appropriate, to meet the goals of this section; and\n**(B)**\nhas, or will establish, partnerships with, and solicit feedback from, other entities in other industries, professional associations, and community- and consumer-focused nonprofit organizations, to meet the goals of this section.\n##### (c) Duties\nAn entity that receives a grant under this section shall\u2014\n**(1)**\ndistribute fair and impartial information concerning eligibility for manufacturer, foundational, and other assistance programs available to patients seeking affordable insulin;\n**(2)**\nfacilitate enrollment in manufacturer assistance programs or other assistance programs for uninsured individuals;\n**(3)**\nmake available to the public, through a standardized website, a clearinghouse of support available to patients, including\u2014\n**(A)**\na link to Federally qualified health centers and other providers, by ZIP Code;\n**(B)**\na link to retail community pharmacies, by ZIP Code; and\n**(C)**\ninformation about how to enroll in health insurance;\n**(4)**\nprovide information in a manner that is culturally and linguistically appropriate;\n**(5)**\nestablish a hotline through which individuals may reach experts with questions about access to insulin, and that\u2014\n**(A)**\nis a 24/7 real-time hotline;\n**(B)**\nprovides voice and text support; and\n**(C)**\nis staffed by navigators or licensed health care professionals;\n**(6)**\nprovide guidance to hospitals on how to share the website and hotline with patients; and\n**(7)**\nconduct public education activities, in collaboration with the Department of Health and Human Services, to raise awareness of the availability of all manufacturer, foundational, and other assistance programs available to patients seeking affordable insulin, with a focus on uninsured individuals; including by\u2014\n**(A)**\npartnering with community health centers, hospitals, retail community pharmacies, and community-based organizations with a focus on access to affordable medicine; and\n**(B)**\nworking with State and local health departments to target the programs carried out using the grant to underserved communities.\n##### (d) Duties of the Secretary\nThe Secretary shall\u2014\n**(1)**\nensure adequate maintenance of the resource center established by the entity receiving a grant under subsection (a);\n**(2)**\npublicize such resource center on the website of the Department of Health and Human Services and across Federal agencies, as the Secretary determines appropriate; and\n**(3)**\nensure that such resource center meets the standards under subsection (e), and withdraw the grant and make an award to a different eligible entity in the case that an eligible entity fails to meet such standards.\n##### (e) Standards\nThe Secretary shall establish standards for the resource center under this section, including provisions to ensure that the entity receiving a grant under this section is qualified to engage in the activities described in this section and to avoid conflicts of interest. Under such standards, such entity\u2014\n**(1)**\nshall not\u2014\n**(A)**\nbe a manufacturer of insulin products; or\n**(B)**\nreceive any consideration directly or indirectly from any manufacturer of insulin products in connection with the enrollment of any individuals in an assistance program; and\n**(2)**\nshall provide information that is fair, accurate, and impartial.\n##### (f) Data collection and evaluations\nThe Secretary may collect data and conduct evaluations with respect to the services provided by the resource center described in this section for purposes of assessing the extent to which the provision of the services\u2014\n**(1)**\nreduces out of pocket insulin costs for uninsured individuals;\n**(2)**\nincreases awareness of assistance programs or foundational support available for uninsured individuals; and\n**(3)**\nimproves utilization of the resources described in paragraph (2) by uninsured individuals.\n##### (g) Reports to Congress\nThe Secretary shall submit to the Committee on Health, Education, Labor, and Pensions and the Committee on Appropriations of the Senate and the Committee on Energy and Commerce and the Committee on Appropriations of the House of Representatives, and make publicly available, annual reports on the activities carried out under this section, including any changes in the availability or scope of assistance programs offered by insulin manufacturers and information about the number of individuals who use the resource center, including the website or hotline.\n##### (h) Definitions\nIn this section\u2014\n**(1)**\nthe term assistance program means a program to assist patients in obtaining a drug at a reduced cost, and includes third-party payments, financial assistance, discounts, product vouchers, and other reductions in out-of-pocket expenses;\n**(2)**\nthe term Federally-qualified health center has the meaning given such term in section 1905(l)(2) of the Social Security Act ( 42 U.S.C. 1396d(l)(2) );\n**(3)**\nthe term insulin means insulin that is licensed under subsection (a) or (k) of section 351 of the Public Health Service Act ( 42 U.S.C. 262 ) and continues to be marketed pursuant to such licensure;\n**(4)**\nthe term retail community pharmacy has the meaning given such term in section 1927(k)(10) of the Social Security Act ( 42 U.S.C. 1396r\u20138(k)(10) ); and\n**(5)**\nthe term uninsured individual means an individual who\u2014\n**(A)**\ndoes not qualify for coverage under a Federal health care program (as defined in section 1128B(f) of the Social Security Act (42 U.S.C. 1320a\u20137b(f))), the health program established under chapter 89 of title 5, United States Code, or a group health plan or group health insurance coverage (as defined in section 2791 of the Public Health Service Act ( 42 U.S.C. 300gg\u201391 )); and\n**(B)**\nis not entitled to a premium assistance tax credit under section 36B of the Internal Revenue Code of 1986.\n##### (i) Funding\nTo carry out this section, there are authorized to be appropriated $2,000,000 for each of fiscal years 2027 through 2032.",
      "versionDate": "2026-03-25",
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
        "actionDate": "2025-10-16",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "3014",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Ensuring Timely Access to Generics Act of 2025",
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
        "name": "Health",
        "updateDate": "2026-04-13T13:47:20Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4189is.xml"
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
      "title": "INSULIN Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T11:03:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "INSULIN Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improving Needed Safeguards for Users of Lifesaving Insulin Now Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reduce the price of insulin and provide for patient protections with respect to the cost of insulin.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:36Z"
    }
  ]
}
```
