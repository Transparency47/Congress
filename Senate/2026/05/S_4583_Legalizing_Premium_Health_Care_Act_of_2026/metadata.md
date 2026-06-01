# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4583?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4583
- Title: Legalizing Premium Health Care Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4583
- Origin chamber: Senate
- Introduced date: 2026-05-20
- Update date: 2026-05-29T07:23:31Z
- Update date including text: 2026-05-29T07:23:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-20: Introduced in Senate
- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-05-20: Introduced in Senate

## Actions

- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4583",
    "number": "4583",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "P000603",
        "district": "",
        "firstName": "Rand",
        "fullName": "Sen. Paul, Rand [R-KY]",
        "lastName": "Paul",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Legalizing Premium Health Care Act of 2026",
    "type": "S",
    "updateDate": "2026-05-29T07:23:31Z",
    "updateDateIncludingText": "2026-05-29T07:23:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-20",
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
          "date": "2026-05-20T16:58:31Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4583is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4583\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2026 Mr. Paul (for himself and Ms. Murkowski ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to establish a Medicare payment option for patients and eligible professionals to freely contract, without penalty, for Medicare fee-for-service items and services, while allowing Medicare beneficiaries to use their Medicare benefits.\n#### 1. Short title\nThis Act may be cited as the Legalizing Premium Health Care Act of 2026 .\n#### 2. Guaranteeing freedom of choice and contracting for patients under Medicare\n##### (a) In general\nSection 1802 of the Social Security Act ( 42 U.S.C. 1395a ) is amended to read as follows:\n1802. Freedom of Choice and Contracting by Patient Guaranteed (a) Basic freedom of choice Any individual entitled to insurance benefits under this title may obtain health services from any institution, agency, or person qualified to participate under this title if such institution, agency, or person undertakes to provide that individual such services. (b) Freedom To contract by Medicare beneficiaries (1) In general Subject to the provisions of this subsection, nothing in this title shall prohibit a Medicare beneficiary from entering into a contract with an eligible professional (whether or not the professional is a participating or non-participating physician or practitioner) for any item or service covered under this title. (2) Submission of claims Any Medicare beneficiary that enters into a contract under this section with an eligible professional shall be permitted to submit a claim for payment under this title for services furnished by such professional, and such payment shall be made in the amount that would otherwise apply to such professional under this title except that where such professional is considered to be non-participating, payment shall be paid as if the professional were participating. Payment made under this title for any item or service provided under the contract shall not render the professional a participating or non-participating physician or practitioner, and as such, requirements of this title that may otherwise apply to a participating or non-participating physician or practitioner would not apply with respect to any items or services furnished under the contract. (3) Beneficiary protections (A) In general Paragraph (1) shall not apply to any contract unless\u2014 (i) the contract is in writing, is signed by the Medicare beneficiary and the eligible professional, and establishes all terms of the contract (including specific payment for items and services covered by the contract) before any item or service is provided pursuant to the contract, and the beneficiary shall be held harmless for any subsequent payment charged for an item or service in excess of the amount established under the contract during the period the contract is in effect; (ii) the contract contains the items described in subparagraph (B); and (iii) the contract is not entered into at a time when the Medicare beneficiary is facing an emergency medical condition or urgent health care situation. (B) Items required to be included in contract Any contract to provide items and services to which paragraph (1) applies shall clearly indicate to the Medicare beneficiary that by signing such contract the beneficiary\u2014 (i) agrees to be responsible for payment to such eligible professional for such items or services under the terms of and amounts established under the contract; (ii) agrees to be responsible for submitting claims under this title to the Secretary, and to any other supplemental insurance plan that may provide supplemental insurance, for such items or services furnished under the contract if such items or services are covered by this title, unless otherwise provided in the contract under subparagraph (C)(i); and (iii) acknowledges that no limits or other payment incentives that may otherwise apply under this title (such as the limits under subsection (g) of section 1848 or incentives under subsection (a)(5), (m), (p), and (q) of such section) shall apply to amounts that may be charged, or paid to a beneficiary for, such items or services. Such contract shall also clearly indicate whether the eligible professional is excluded from participation under the Medicare program under section 1128. (C) Beneficiary elections under the contract Any Medicare beneficiary that enters into a contract under this section may elect to negotiate, as a term of the contract, a provision under which\u2014 (i) the eligible professional shall file claims on behalf of the beneficiary with the Secretary and any supplemental insurance plan for items or services furnished under the contract if such items or services are covered under this title or under the plan; and (ii) the beneficiary assigns payment to the eligible professional for any claims filed by, or on behalf of, the beneficiary with the Secretary and any supplemental insurance plan for items or services furnished under the contract. (D) Exclusion of dual eligible individuals Paragraph (1) shall not apply to any contract if a beneficiary who is eligible for medical assistance under title XIX is a party to the contract. (4) Limitation on actual charge and claim submission requirement not applicable Section 1848(g) shall not apply with respect to any item or service provided to a Medicare beneficiary under a contract described in paragraph (1). (5) Construction Nothing in this section shall be construed\u2014 (A) to prohibit any eligible professional from maintaining an election and acting as a participating or non-participating physician or practitioner with respect to any patient not covered under a contract established under this section; and (B) as changing the items and services for which an eligible professional may bill under this title. (6) Definitions In this subsection: (A) Medicare beneficiary The term Medicare beneficiary means an individual who is entitled to benefits under part A or enrolled under part B. (B) Eligible professional The term eligible professional has the meaning given such term in section 1848(k)(3)(B). (C) Emergency medical condition The term emergency medical condition means a medical condition manifesting itself by acute symptoms of sufficient severity (including severe pain) such that a prudent layperson, with an average knowledge of health and medicine, could reasonably expect the absence of immediate medical attention to result in\u2014 (i) serious jeopardy to the health of the individual or, in the case of a pregnant woman, the health of the woman or her unborn child; (ii) serious impairment to bodily functions; or (iii) serious dysfunction of any bodily organ or part. (D) Participating; non-participating The terms participating and nonparticipating have the meanings given such terms under subsection (h) of section 1842 for purposes of such section. (E) Urgent health care situation The term urgent health care situation means services furnished to an individual who requires services to be furnished within 12 hours in order to avoid the likely onset of an emergency medical condition. .\n##### (b) Conforming amendment\nSection 1814(a)(7)(D)(i)(II) of the Social Security Act ( 42 U.S.C. 1395f(a)(7)(D)(i)(II) ) is amended by striking and is not an opt-out physician or practitioner (as defined in section 1802(b)(6)(D)) .\n#### 3. Preemption of State laws limiting charges for services by an eligible professional\n##### (a) In general\nNo State may impose a limit on the amount of charges for services, furnished by an eligible professional (as defined in subsection (k)(3)(B) of section 1848 of the Social Security Act, 42 U.S.C. 1395w\u20134 ), for which payment is made under such section, and any such limit is hereby preempted.\n##### (b) State\nIn this section, the term State includes the District of Columbia, Puerto Rico, the Virgin Islands, Guam, and American Samoa.",
      "versionDate": "2026-05-20",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4583is.xml"
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
      "title": "Legalizing Premium Health Care Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-29T07:23:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Legalizing Premium Health Care Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-29T07:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to establish a Medicare payment option for patients and eligible professionals to freely contract, without penalty, for Medicare fee-for-service items and services, while allowing Medicare beneficiaries to use their Medicare benefits.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-29T07:18:35Z"
    }
  ]
}
```
