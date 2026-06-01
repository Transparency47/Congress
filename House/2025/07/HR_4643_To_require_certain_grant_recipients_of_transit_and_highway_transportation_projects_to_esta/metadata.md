# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4643?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4643
- Title: Business Uninterrupted Monetary Program Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4643
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-04-14T18:21:30Z
- Update date including text: 2026-04-14T18:21:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-24 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-24 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4643",
    "number": "4643",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001110",
        "district": "46",
        "firstName": "J.",
        "fullName": "Rep. Correa, J. Luis [D-CA-46]",
        "lastName": "Correa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Business Uninterrupted Monetary Program Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-14T18:21:30Z",
    "updateDateIncludingText": "2026-04-14T18:21:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-24T21:27:55Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4643ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4643\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Correa (for himself and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require certain grant recipients of transit and highway transportation projects to establish and contribute to a business uninterrupted monetary program fund, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Business Uninterrupted Monetary Program Act of 2025 .\n#### 2. Fixed guideway capital investment grants\nSection 5309 of title 49, United States Code, is amended by adding at the end the following:\n(s) Business uninterrupted monetary program fund (1) Establishment To be eligible for a grant under this section, a project sponsor or shall establish a fund to be known as a business uninterrupted monetary program fund (in this subsection referred to as a BUMP Fund ). (2) Fund requirements Amounts contributed to a BUMP Fund under this subsection\u2014 (A) may count toward the non-Federal share of the cost of a project under such section; and (B) shall be provided to covered entities that are negatively impacted by an interruption caused by a project carried out with amounts made available under such grant. (3) Contributions to the Fund (A) In general The Secretary shall require that the project sponsor contribute an amount into a BUMP Fund that meets the following requirements: (i) The amount required to be set aside shall not impact the total project cost or the total non-Federal match requirement of the project. (ii) Such amount shall reflect the funds necessary to fully carry out the requirement described in paragraph (2)(B). (iii) Such amount may not constitute an amount of the non-Federal cost share that would impede the project sponsor from carrying out the project. (iv) Apply to projects with total cost equal or greater than $100 million. (v) Such amount shall be determined by the local sponsor, so long as such amount\u2014 (I) does not exceed 10 percent of the total non-Federal share; and (II) reflects the estimated damages caused by the interruption. (B) Waiver The Secretary may waive or alter the percentage of the contribution amount required under subparagraph (A)\u2014 (i) if the Secretary determines that the project sponsor has an equivalent program established that is applicable to the project; (ii) the Secretary determines that there is no interruption that could occur with respect to a project; (iii) the amount of Federal funding for the total cost of the project is less than 10 percent of such cost; or (iv) for any other reason the Secretary determines appropriate. (4) Eligibility for receipt of funds The applicant, as part of the portion of the application for a grant under this section that relates to the financial commitment of the applicant, shall provide information to the Secretary on how the project sponsor shall determine which covered entities are eligible to receive assistance from a BUMP Fund, including the following: (A) Which covered entities are eligible to receive funding under the BUMP Fund. (B) The terms for eligibility for amounts in a BUMP Fund. (C) The process by which the local sponsor or project partner shall\u2014 (i) determine the impact on covered entities; (ii) distribute the funds to covered entities; and (iii) verify the information provided by covered entities. (D) The total funding available per covered entity. (E) The outreach plan for informing covered entities. (F) Any other information the applicant determines is necessary. (5) Eligible expenses (A) In general Eligible expenses provided to a covered entity from a BUMP Fund may include, at the discretion of the project sponsor, the following: (i) Utilities. (ii) Insurance. (iii) Rent or mortgage. (iv) Payroll. (v) Loss of income. (vi) Any other expense the sponsor determines is consistent with the requirements of this section. (B) Invalidation of payment by Secretary The Secretary may disqualify an eligible expense submitted by a project sponsor at the time such recipient submits its financial commitment if the Secretary determines such an expense is not consistent with the requirements of this section. (6) Combined BUMP Fund For a project sponsor that has more than 2 projects running concurrently, the project sponsor may maintain one BUMP Fund to cover all such projects. (7) Retention of funds Funds set aside for the BUMP Fund shall remain available for a period of 1 year after the completion of the project for which the BUMP Fund was established unless the project sponsor certifies to the Secretary that the funds are no longer needed. (8) Unused funds Any amounts deposited in a BUMP Fund that are not dispensed during the project may be available to the recipient for the following uses: (A) Operating expenses for the project for which the BUMP Fund was established. (B) Project enhancements or construction cost overruns for the project. (C) Other projects eligible under this title, except that the amounts may not count toward non-Federal matching funds of any other project. (D) In any case in which the recipient does not manage the project, amounts may be returned to the grant recipient. (E) For any other purpose approved by the Secretary. (9) Derivation of funds for deposit into BUMP Fund The funds dedicated to a BUMP Fund may be derived from\u2014 (A) non-Federal funds, unless deposit of such non-Federal funds is prohibited by the terms of an agreement between the funding source and the project sponsor; or (B) Federal funds, if approved by the Secretary. (10) Definitions In this subsection: (A) Business uninterrupted monetary program fund; BUMP Fund The term business uninterrupted monetary program fund or BUMP Fund means a fund for the purpose of providing financial assistance to covered entities directly and negatively impacted by a transportation project funded by a grant under this section to reimburse such a covered entity for expenses incurred during an interruption caused by such project. (B) Covered entity The term covered entity means a private business or nonprofit organization, as defined by the project sponsor. (C) Interruption The term \u2018interruption\u2019 means an activity carried out as part of a project for which a grant is provided under this section that disrupts the activities of a covered entity and causes measurable negative impacts to the financial well-being of such entity. (D) Project sponsor The term project sponsor means the sponsor of a project, or affiliated project partner, for which a grant is provided under this section. .\n#### 3. Federal-aid highway program\n##### (a) In general\nChapter 1 of title 23, United States Code, is amended by adding at the end the following:\n180. Business uninterrupted monetary program fund (a) Business Uninterrupted Monetary Program Fund (1) Establishment The Secretary shall require a recipient of Federal-aid highway funds under this title to establish a fund to be known as a business uninterrupted monetary program fund (in this section referred to as a Bump Fund ) as required under section 106(k). (2) Fund requirements Amounts contributed to a BUMP Fund under this section\u2014 (A) may count toward the non-Federal share of the cost of a covered project; and (B) shall be provided to covered entities that are negatively impacted by an interruption cause by a covered project. (3) Contributions to the Fund (A) In general The Secretary shall require that the project sponsor of a covered project contribute an amount into a BUMP Fund that meets the following requirements: (i) The amount required to be set aside shall not impact the total non-Federal match requirement of the project. (ii) Such amount shall reflect the funds necessary to fully carry out the requirement described in paragraph (2)(B). (iii) Such amount may not constitute an amount of the non-Federal cost share that would impede the project sponsor from carrying out the project. (iv) The amount allocated to the BUMP fund shall be determined by the local sponsor, so long as\u2014 (I) the amount does not exceed 25 percent of the total non-Federal share; and (II) the amount reflects the estimated damages caused by the interruption. (B) Waiver The Secretary may waive or alter the percentage of the contribution amount required under subparagraph (A)\u2014 (i) if the Secretary determines that the project sponsor has an equivalent program established that is applicable to the project; (ii) the Secretary determines that there is no interruption that could occur with respect to a project; (iii) the amount of Federal funding for the total cost of the project is less than 10 percent of such cost; or (iv) for any other reason the Secretary determines appropriate. (4) Eligibility for receipt of funds An applicant for funds for a covered project, as part of the portion of the application that relates to the financial commitment of the applicant, shall provide information to the Secretary on the implementation of BUMP Fund including the following: (A) Which covered entities are eligible to receive funding under the BUMP Fund. (B) The terms for eligibility for amounts in a BUMP Fund. (C) The process by which the local sponsor or project partner shall\u2014 (i) determine the impact on covered entities; (ii) distribute the funds to covered entities; and (iii) verify the information provided by covered entities. (D) The total funding available per covered entity. (E) The outreach plan for informing covered entities. (F) Any other information the applicant determines is necessary. (5) Eligible expenses (A) In general Eligible expenses provided to a covered entity from a BUMP Fund may include, at the discretion of the project sponsor, the following: (i) Utilities for the covered entity. (ii) Insurance for the covered entity and employees of such entity. (iii) Rent or mortgage payments. (iv) Payroll expenses. (v) Loss of income. (vi) Any other expense the sponsor determines is consistent with the requirements of this section. (B) Invalidation of payment by Secretary The Secretary may disqualify an eligible expense submitted by a project sponsor at the time such recipient submits its financial commitment if the Secretary determines such an expense is not consistent with the requirements of this section. (6) Retention of funds Funds set aside for the BUMP Fund shall remain available for a period of 1 year after the completion of the project for which the BUMP Fund was established unless the project sponsor certifies to the Secretary that the funds are no longer needed. (7) Unused funds Any amounts deposited in a BUMP Funds that are not dispensed during the project may be available to the project sponsor for the following uses: (A) Project enhancements, including non-infrastructure project enhancements, or construction cost overruns for the project. (B) Environmental mitigation described under section 119(g) of title 23, United States Code. (C) Other projects eligible under this title, except that the amounts may not count toward non-Federal matching funds of any other project. (D) In any case in which the project sponsor does not manage the project, amounts may be returned to the initial recipient of the Federal funds provided for the covered project. (E) For any other purpose approved by the Secretary. (8) Derivation of funds for deposit into BUMP Fund The funds dedicated to BUMP Fund may be derived from\u2014 (A) a non-Federal source, consistent with the requirements of part 200 of title 2, Code of Federal Regulations, unless deposit of such non-Federal funds is prohibited by the terms of an agreement between the funding source and the project sponsor; or (B) Federal funds, if approved by the Secretary. (9) Projects without a non-Federal share For any covered project that is funded with 100 percent Federal funds, the Secretary shall determine, together with the project sponsor, an appropriate amount of funding for the BUMP Fund. (10) Combined BUMP Fund For a project sponsor that has more than 2 projects running concurrently, the project sponsor may maintain one BUMP Fund to cover all such projects. (b) Definitions In this section: (1) Business uninterrupted monetary program fund; BUMP Fund The term business uninterrupted monetary program fund or BUMP Fund means a fund for the purpose of providing financial assistance to covered entities directly and negatively impacted by covered project to reimburse such a covered entity for expenses incurred during an interruption caused by such project. (2) Covered entity The term covered entity means a private business or nonprofit organization, as defined by the project sponsor. (3) Covered project The term covered project means any project carried out under this title that has a total cost of $50,000,000 or greater. (4) Interruption The term \u2018interruption\u2019 means an activity carried out as part of a covered project that disrupts the activities of a covered entity and causes measurable negative impacts to the financial well-being of such entity. (5) Project sponsor The term project sponsor means the entity or affiliated project partner carrying out a covered project. .\n##### (b) Clerical amendment\nThe analysis for chapter 1 of title 23, United States Code, is amended by adding at the end the following:\n180. Business uninterrupted monetary program fund. .\n##### (c) Project approval and oversight\nSection 106 of title 23, United States Code, is amended by adding at the end the following:\n(k) Business uninterrupted monetary program fund A recipient of Federal financial assistance under this title for a project with an estimated total project cost of $50,000,000 or more shall establish a business uninterrupted monetary program fund as described under section 180, and subject to the requirements of such section, to address financial impacts to companies that suffer financial burdens as a result of project construction. .\n#### 4. Grants for certain interruptions due to fixed guideway capital investment projects\n##### (a) Establishment\nNot later than 270 days after the date of enactment of this Act, the Secretary of Transportation shall establish a competitive grant program that provides a single round of grants to project sponsors to provide relief to covered entities as described in section 5309(s) of title 49, United States Code (as added by section 2).\n##### (b) Eligibility\nA project sponsor is eligible for a grant under subsection (a) for any project\u2014\n**(1)**\nthat meets the requirements of section 5309(s) of title 49, United States Code;\n**(2)**\nfor which construction began on or after October 1, 2018; and\n**(3)**\nthat remains under construction as of June 1, 2023.\n##### (c) Funding limitations\nA grant provided under this section may not exceed $10,000,000.\n##### (d) Unused amounts\nAny funds not made available pursuant to this section shall be retained in the account to which the funds were appropriated and made available for any other purpose provided for by law.\n##### (e) Definitions\nThe definitions in section 5309(s)(9) of title 49, United States Code, shall apply to this section.\n#### 5. Implementation\nThe Secretary of Transportation shall implement the requirements of the amendments made by sections 2 and 3 of this Act not later than 270 days after the date of enactment of this Act.",
      "versionDate": "2025-07-23",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-04-14T18:21:30Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4643ih.xml"
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
      "title": "Business Uninterrupted Monetary Program Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-07T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Business Uninterrupted Monetary Program Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require certain grant recipients of transit and highway transportation projects to establish and contribute to a business uninterrupted monetary program fund, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-07T05:18:31Z"
    }
  ]
}
```
