# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3599?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3599
- Title: Affordable CHOICE Act
- Congress: 119
- Bill type: S
- Bill number: 3599
- Origin chamber: Senate
- Introduced date: 2026-01-08
- Update date: 2026-03-13T15:59:41Z
- Update date including text: 2026-03-13T15:59:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-08: Introduced in Senate
- 2026-01-08 - IntroReferral: Introduced in Senate
- 2026-01-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-01-08: Introduced in Senate

## Actions

- 2026-01-08 - IntroReferral: Introduced in Senate
- 2026-01-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-08",
    "latestAction": {
      "actionDate": "2026-01-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3599",
    "number": "3599",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Affordable CHOICE Act",
    "type": "S",
    "updateDate": "2026-03-13T15:59:41Z",
    "updateDateIncludingText": "2026-03-13T15:59:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-08",
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
      "actionDate": "2026-01-08",
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
          "date": "2026-01-08T16:23:50Z",
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
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3599is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3599\nIN THE SENATE OF THE UNITED STATES\nJanuary 8 (legislative day, January 7), 2026 Mr. Whitehouse (for himself and Ms. Slotkin ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Patient Protection and Affordable Care Act to establish a public health insurance option, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Affordable Consumer Health Options and Insurance Competition Enhancement Act or the Affordable CHOICE Act .\n#### 2. Public health insurance option\n##### (a) In general\nPart 2 of subtitle D of title I of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18031 et seq. ) is amended by adding at the end the following:\n1314. Public health insurance option (a) Establishment (1) In general For plan years beginning on or after January 1, 2027, the Secretary shall establish, and provide for the offering through the Exchanges of, a qualified health plan (in this section referred to as the public health insurance option ) that provides value, choice, competition, and stability of affordable, high-quality coverage throughout the United States in accordance with this section. (2) Primary responsibility In designing the public health insurance option, the primary responsibility of the Secretary shall be to create an affordable health plan without compromising quality or access to care. (b) Administrating the public health insurance option (1) Offered through Exchanges (A) Exclusive to Exchanges The public health insurance option shall be offered exclusively by the Secretary through the Exchanges and not by a health insurance issuer. (B) Ensuring a level playing field Except as otherwise provided under this section, the public health insurance option shall comply with requirements under this title, and title XXVII of the Public Health Service Act, that are applicable to health plans offered through the Exchanges, including requirements related to benefits, benefit levels, provider networks, notices, consumer protections, and cost-sharing. (C) Provision of benefit levels The public health insurance option shall offer bronze, silver, and gold plans. (2) Administrative contracting (A) Authorities The Secretary may enter into contracts for the purpose of performing administrative functions (including functions described in subsection (a)(4) of section 1874A of the Social Security Act) with respect to the public health insurance option in the same manner as the Secretary may enter into contracts under subsection (a)(1) of such section. The Secretary shall have the same authority with respect to the public health insurance option as the Secretary has under such subsection (a)(1) and subsection (b) of section 1874A of the Social Security Act with respect to title XVIII of such Act. (B) Transfer of insurance risk Any contract under this paragraph shall not involve the transfer of insurance risk from the Secretary to the entity entering into such contract with the Secretary. (3) State Advisory Council (A) Establishment A State may establish a public or nonprofit entity to serve as the State Advisory Council to provide recommendations to the Secretary on the operations and policies of the public health insurance option offered through the Exchange operating in the State. (B) Recommendations A State Advisory Council established under subparagraph (A) shall provide recommendations on at least the following: (i) Policies and procedures to integrate quality improvement and cost containment mechanisms into the health care delivery system. (ii) Mechanisms to facilitate public awareness of the availability of the public health insurance option. (iii) Alternative payment models and value-based insurance design under the public health insurance option that encourage quality improvement and cost control. (C) Members The members of any State Advisory Council shall be representatives of the public and include health care consumers and health care providers. (D) Applicability of recommendations The Secretary may apply the recommendations of a State Advisory Council to the public health insurance option in that State, in any other State, or in all States. (4) Data collection The Secretary shall collect such data as may be required\u2014 (A) to establish rates for premiums and health care provider reimbursement under subsection (c); and (B) for other purposes under this section, including to improve quality, and reduce racial, ethnic, and other disparities, in health and health care. (c) Financing the public health insurance option (1) Premiums (A) Establishment The Secretary shall establish geographically adjusted premium rates for the public health insurance option\u2014 (i) in a manner that complies with the requirement for premium rates under subparagraph (C) and considers the data collected under subsection (b)(4); and (ii) at a level sufficient to fully finance\u2014 (I) the costs of health benefits provided by the public health insurance option; and (II) administrative costs related to operating the public health insurance option. (B) Contingency margin In establishing premium rates under subparagraph (A), the Secretary shall include an appropriate amount for a contingency margin. (C) Variations in premium rates The premium rate charged for the public health insurance option may not vary except as provided under section 2701 of the Public Health Service Act. (2) Health care provider payment rates for items and services (A) In general (i) Rates negotiated by the Secretary Not later than January 1, 2026, and except as provided in clause (ii), the Secretary shall, through a negotiated agreement with health care providers, establish rates for reimbursing health care providers for providing the benefits covered by the public health insurance option. (ii) Medicare reimbursement rates If the Secretary and health care providers are unable to reach a negotiated agreement on a reimbursement rate, the Secretary shall reimburse providers at rates determined for equivalent items and services under the original Medicare fee-for-service program under parts A and B of title XVIII of the Social Security Act. (iii) For new services The Secretary shall modify reimbursement rates described in clause (ii) in order to accommodate payments for services, such as well-child visits, that are not otherwise covered under the original Medicare fee-for-service program. (B) Prescription drugs Any payment rate under this subsection for a prescription drug shall be at a rate negotiated by the Secretary. If the Secretary is unable to reach a negotiated agreement on such a reimbursement rate, the Secretary shall use rates determined for equivalent drugs paid for under the original Medicare fee-for-service program. The Secretary shall modify such rates in order to accommodate payments for drugs that are not otherwise covered under the original Medicare fee-for-service program. (3) Account (A) Establishment There is established in the Treasury of the United States an account for the receipts and disbursements attributable to the operation of the public health insurance option, including the start-up funding under subparagraph (C) and appropriations authorized under subparagraph (D). (B) Prohibition of State imposition of taxes Section 1854(g) of the Social Security Act shall apply to receipts and disbursements described in subparagraph (A) in the same manner as such section applies to payments or premiums described in such section. (C) Start-up funding (i) Authorization of funding There are authorized to be appropriated such sums as may be necessary to establish the public health insurance option and cover 90 days of claims reserves based on projected enrollment. (ii) Amortization of start-up funding The Secretary shall provide for the repayment of the start-up funding provided under clause (i) to the Treasury in an amortized manner over the 10-year period beginning on January 1, 2027. (D) Additional authorization of appropriations To carry out paragraph (2) of subsection (b), there are authorized to be appropriated such sums as may be necessary. (d) Health care provider participation (1) Provider participation (A) In general The Secretary shall establish conditions of participation for health care providers under the public health insurance option. (B) Licensure or certification The Secretary shall not allow a health care provider to participate in the public health insurance option unless such provider is appropriately licensed or certified under State law. (2) Establishment of a provider network (A) Medicare and Medicaid participating providers A health care provider that is a participating provider of services or supplier under the Medicare program under title XVIII of the Social Security Act or under a State Medicaid plan under title XIX of such Act is a participating provider in the public health insurance option unless the health care provider opts out of participating in the public health insurance option through a process established by the Secretary. (B) Additional providers The Secretary shall establish a process to allow health care providers not described in subparagraph (A) to become participating providers in the public health insurance option. .\n##### (b) Conforming amendments\n**(1) Treatment as a qualified health plan**\nSection 1301(a) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18021(a) ) is amended\u2014\n**(A)**\nin paragraph (1)(C), by inserting except in the case of the public health insurance option established under section 1314, before is offered by ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin the paragraph heading, by inserting , the public health insurance option, before and ; and\n**(ii)**\nby inserting the public health insurance option under section 1314, before and a multi-State plan ; and\n**(C)**\nby adding at the end the following:\n(5) Public health insurance option The term qualified health plan shall include the public health insurance option established under section 1314. .\n**(2) Level playing field**\nSection 1324(a) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18044(a) ) is amended by inserting the public health insurance option under section 1314, before or a multi-State qualified health plan .",
      "versionDate": "2026-01-08",
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
        "actionDate": "2026-01-12",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "7023",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Affordable CHOICE Act",
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
        "name": "Health",
        "updateDate": "2026-02-11T17:57:37Z"
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
      "date": "2026-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3599is.xml"
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
      "title": "Affordable CHOICE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-07T05:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Affordable CHOICE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-07T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Affordable Consumer Health Options and Insurance Competition Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-07T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Patient Protection and Affordable Care Act to establish a public health insurance option, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-07T05:03:33Z"
    }
  ]
}
```
