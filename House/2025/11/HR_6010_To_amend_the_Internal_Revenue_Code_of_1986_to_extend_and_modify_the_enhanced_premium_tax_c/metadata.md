# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6010?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6010
- Title: To amend the Internal Revenue Code of 1986 to extend and modify the enhanced premium tax credit, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 6010
- Origin chamber: House
- Introduced date: 2025-11-10
- Update date: 2025-12-11T15:11:39Z
- Update date including text: 2025-12-11T15:11:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-10: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-10 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-11-10: Introduced in House

## Actions

- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-10 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-10",
    "latestAction": {
      "actionDate": "2025-11-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6010",
    "number": "6010",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000607",
        "district": "16",
        "firstName": "Sam",
        "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
        "lastName": "Liccardo",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to extend and modify the enhanced premium tax credit, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-12-11T15:11:39Z",
    "updateDateIncludingText": "2025-12-11T15:11:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-10",
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
      "actionDate": "2025-11-10",
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
      "actionDate": "2025-11-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-10",
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
          "date": "2025-11-10T17:03:35Z",
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
          "date": "2025-11-10T17:03:30Z",
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
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "CA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "NE"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "NH"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "NC"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "NY"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "IA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "CA"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "WA"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "CA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "NJ"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-12-05",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6010ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6010\nIN THE HOUSE OF REPRESENTATIVES\nNovember 10, 2025 Mr. Liccardo (for himself, Mr. Kiley of California , Mr. Bacon , Ms. Goodlander , and Ms. Ross ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Internal Revenue Code of 1986 to extend and modify the enhanced premium tax credit, and for other purposes.\n#### 1. Temporary premium percentages for 2026 and 2027\n##### (a) In general\nSection 36B(b)(3)(A)(iii) of the Internal Revenue Code of 1986 is amended to read as follows:\n(iii) Temporary percentages for 2026 and 2027 In the case of a taxable year beginning after December 31, 2025, and before January 1, 2028, the following table shall be applied in lieu of the table contained in clause (i): In the case of household income (expressed as a percent of poverty line) within the following income tier: The initial premium percentage is\u2014 The final premium percentage is\u2014 Up to 150 percent 0.0 0.0 150 percent up to 200 percent 0.0 2.0 200 percent up to 250 percent 2.0 4.0 250 percent up to 300 percent 4.0 6.0 300 percent up to 400 percent 6.0 8.5 400 percent up to 600 percent 8.5 8.5 .\n##### (b) Conforming amendment\nSection 36B(c)(1)(E) of such Code is amended to read as follows:\n(E) Temporary rule for 2026 and 2027 In the case of a taxable year beginning after December 31, 2025, and before January 1, 2028, subparagraph (A) shall be applied by substituting 600 percent for 400 percent . .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 2. Improving risk adjustment under Medicare Advantage\n##### (a) Use of 2 years of diagnostic data\nSection 1853(a)(3)(C)(iii) of the Social Security Act ( 42 U.S.C. 1395w\u201323(a)(3)(C)(iii) ) is amended\u2014\n**(1)**\nby striking methodology .\u2014Such risk and inserting \u201c methodology .\u2014\n(I) In general Subject to subclause (II), such risk ; and\n**(2)**\nby adding at the end the following new subclause:\n(II) Use of health status data For 2026 and each subsequent year, the Secretary shall use 2 years of diagnostic data (when available) under such risk adjustment methodology. .\n##### (b) Exclusion of diagnoses collected from chart reviews and health risk assessments\nSection 1853(a)(1)(C) of such Act ( 42 U.S.C. 1395w\u201323(a)(1)(C) ) is amended by adding at the end the following new clause:\n(iv) Exclusion of diagnoses collected from chart reviews and health risk assessments (I) In general For 2026 and each subsequent year, for purposes of establishing the payment adjustment factors and adjusting payment based on health status under clause (i), the Secretary shall not take into account a diagnosis collected from a chart review or a health risk assessment. (II) Identification of diagnoses collected from chart reviews and health risk assessments The Secretary shall establish procedures to provide for the identification and verification of diagnoses collected from chart reviews and health risk assessments. .\n##### (c) Application of coding adjustment\nSection 1853(a)(1)(C)(ii) of such Act ( 42 U.S.C. 1395w\u201323(a)(1)(C)(ii) ) is amended\u2014\n**(1)**\nin subclause (III), by striking In calculating and inserting Subject to subclause (V), in calculating ; and\n**(2)**\nby adding at the end the following new subclause:\n(V) In calculating such adjustment for 2026 and each subsequent year, the Secretary shall evaluate the impact on risk scores for Medicare Advantage enrollees of differences in coding patterns between Medicare Advantage plans and providers under parts A and B and publicly report the results of such evaluation. The Secretary shall ensure that such adjustment, which may include adjustment on a plan or contract level, fully accounts for the impact of coding pattern differences not otherwise accounted for to the extent that the Secretary identifies such differences through annual evaluation. .\n#### 3. Reduction of fraudulent enrollment in qualified health plans\n##### (a) Penalties for agents and brokers\nSection 1411(h)(1) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18081(h)(1) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nby redesignating clause (ii) as clause (iv);\n**(B)**\nin clause (i)\u2014\n**(i)**\nin the matter preceding subclause (I), by striking If\u2014 and all that follows through the such person in the matter following subclause (II) and inserting the following: If any person (other than an agent or broker) fails to provide correct information under subsection (b) and such failure is attributable to negligence or disregard of any rules or regulations of the Secretary, such person ; and\n**(ii)**\nin the second sentence, by striking For purposes and inserting the following:\n(iii) Definitions of negligence, disregard For purposes ;\n**(C)**\nby inserting after clause (i) the following:\n(ii) Civil penalties for certain violations by agents or brokers If any agent or broker fails to provide correct information under subsection (b) or section 1311(c)(8) or other information, as specified by the Secretary, and such failure is attributable to negligence or disregard of any rules or regulations of the Secretary, such agent or broker shall be subject, in addition to any other penalties that may be prescribed by law, including subparagraph (C), to a civil penalty of not less than $10,000 and not more than $50,000 with respect to each individual who is the subject of an application for which such incorrect information is provided. ; and\n**(D)**\nin clause (iv) (as so redesignated), by inserting or (ii) after clause (i) ;\n**(2)**\nin subparagraph (B)\u2014\n**(A)**\nby inserting including subparagraph (C), after law, ;\n**(B)**\nby striking Any person and inserting the following:\n(i) In general Any person ; and\n**(C)**\nby adding at the end the following:\n(ii) Civil penalties for knowing violations by agents or brokers (I) In general Any agent or broker who knowingly provides false or fraudulent information under subsection (b) or section 1311(c)(8), or other false or fraudulent information as part of an application for enrollment in a qualified health plan offered through an Exchange, as specified by the Secretary, shall be subject, in addition to any other penalties that may be prescribed by law, including subparagraph (C), to a civil penalty of not more than $200,000 with respect to each individual who is the subject of an application for which such false or fraudulent information is provided. (II) Procedure The provisions of section 1128A of the Social Security Act (other than subsections (a) and (b) of such section) shall apply to a civil monetary penalty under subclause (I) in the same manner as such provisions apply to a penalty or proceeding under section 1128A of the Social Security Act. ; and\n**(3)**\nby adding at the end the following:\n(C) Criminal penalties Any agent or broker who knowingly and willfully provides false or fraudulent information under subsection (b) or section 1311(c)(8), or other false or fraudulent information as part of an application for enrollment in a qualified health plan offered through an Exchange, as specified by the Secretary, shall be fined under title 18, United States Code, imprisoned for not more than 10 years, or both. .\n##### (b) Consumer protections\n**(1) In general**\nSection 1311(c) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18031(c) ) is amended by adding at the end the following:\n(8) Agent-or broker-assisted enrollment in qualified health plans in certain exchanges (A) In general For plan years beginning on or after such date specified by the Secretary, but not later than January 1, 2028, in the case of an Exchange that the Secretary operates pursuant to section 1321(c)(1), the Secretary shall establish a verification process for new enrollments of individuals in, and changes in coverage for individuals under, a qualified health plan offered through such Exchange, which are submitted by an agent or broker in accordance with section 1312(e) and for which the agent or broker is eligible to receive a commission. (B) Requirements The enrollment verification process under subparagraph (A) shall include\u2014 (i) a requirement that the agent or broker provide with the new enrollment or coverage change such documentation or evidence (such as a standardized consent form) or other sources as the Secretary determines necessary to establish that the agent or broker has the consent of the individual for the new enrollment or coverage change; (ii) a requirement that any commissions due to a broker or agent for such new enrollment or coverage change are paid after the enrollee has resolved all inconsistencies in accordance with paragraphs (3) and (4) of section 1411(e); (iii) a requirement that the information required under clause (i) and, as applicable, the date on which inconsistencies are resolved as described in clause (ii), is accessible to the applicable qualified health plan through a database or other resource, as determined by the Secretary, so that any commissions due to a broker or agent for such enrollment can be effectuated at the appropriate time; (iv) a requirement that individuals are notified of any changes to enrollment, coverage, the agent of record, or premium tax credits in a timely manner and that such notice provides plain language instructions on how individuals can cancel unauthorized activity; (v) a requirement that individuals be able to access their account information on a website or other technology platform, as defined by the Secretary, when used to submit an enrollment or plan change, in lieu of the Exchange website described in subsection (d)(4)(C), including information on the agent of record, the qualified health plan, and when any changes are made to the agent of record or the qualified health plan, on a consumer-facing website or through a toll-free telephone hotline; and (vi) a requirement that the agent or broker report to the Secretary any third-party marketing organization or field marketing organization (as such terms are defined in section 1312(e)) involved in the chain of enrollment (as so defined) with respect to such new enrollment or coverage change. (C) Consumer protection The Secretary shall ensure that the enrollment verification process under subparagraph (A) prioritizes continuity of coverage and care for individuals, including by not disenrolling individuals from a qualified health plan without the consent of the individual, regardless of whether the broker, agent, or qualified health plan is in violation of any requirement under this paragraph. .\n**(2) Required reporting**\nSection 1311(c)(1) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18031(c)(1) ) is amended\u2014\n**(A)**\nin subparagraph (H), by striking and at the end;\n**(B)**\nin subparagraph (I), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(J) report to the Secretary the termination (as defined in section 1312(e)(4)(C)) of an issuer. .\n##### (c) Authority To regulate field marketing organizations and third-Party marketing organizations\nSection 1312(e) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18032(e) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (1) and (2) as subclauses (I) and (II), respectively, and adjusting the margins accordingly;\n**(2)**\nin subclause (II) (as so redesignated), by striking the period at the end and inserting ; and ;\n**(3)**\nby striking the subsection designation and heading and all that follows through brokers\u2014 and inserting the following:\n(e) Regulation of agents, brokers, and certain marketing organizations (1) Agents, brokers, and certain marketing organizations (A) In general The Secretary shall establish procedures under which a State may allow\u2014 (i) agents or brokers\u2014 ; and\n**(4)**\nby adding at the end the following:\n(ii) field marketing organizations and third-party marketing organizations to participate in the chain of enrollment for an individual with respect to qualified health plans offered through an Exchange. (B) Criteria For plan years beginning on or after such date specified by the Secretary, but not later than January 1, 2028, the Secretary, by regulation, shall establish criteria for States to use in determining whether to allow agents and brokers to enroll individuals and employers in qualified health plans as described in subclause (I) of subparagraph (A)(i) and to assist individuals as described in subclause (II) of such subparagraph and field marketing organizations and third-party marketing organizations to participate in the chain of enrollment as described in subparagraph (A)(ii). Such criteria shall, at a minimum, require that\u2014 (i) an agent or broker act in accordance with a standard of conduct that includes a duty of such agent or broker to act in the best interests of the enrollee; (ii) a field marketing organization or third-party marketing organization agree to report the termination of an agent or broker to the applicable State and the Secretary, including the reason for termination; and (iii) an agent, broker, field marketing organization, or third-party marketing organization\u2014 (I) meet such marketing requirements as are required by the Secretary; (II) meet marketing requirements in accordance with other applicable Federal or State law; (III) does not employ practices that are confusing or misleading, as determined by the Secretary; (IV) submit all marketing materials to the Secretary for, as determined appropriate by the Secretary, review and approval; (V) is a licensed agent or broker or meets other licensure requirements, as required by the State; (VI) register with the Secretary; and (VII) does not compensate any individual or organization for referrals or any other service relating to the sale of, marketing for, or enrollment in qualified health plans unless such individual or organization meets the criteria described in subclauses (I) through (VI). (C) Definitions In this paragraph: (i) Chain of enrollment The term chain of enrollment , with respect to enrollment of an individual in a qualified health plan offered through an Exchange, means any steps taken from marketing to such individual, to such individual making an enrollment decision with respect to such a plan. (ii) Field marketing organization The term field marketing organization means an organization or individual that directly employs or contracts with agents and brokers, or contracts with carriers, to provide functions relating to enrollment of individuals in qualified health plans offered through an Exchange as part of the chain of enrollment. (iii) Marketing The term marketing means the use of marketing materials to provide information to current and prospective enrollees in a qualified health plan offered through an Exchange. (iv) Marketing materials The term marketing materials means materials relating to a qualified health plan offered through an Exchange or benefits offered through an Exchange that\u2014 (I) are intended\u2014 (aa) to draw an individual\u2019s attention to such plan or the premium tax credits or cost-sharing reductions for such plan or plans offered through an Exchange; (bb) to influence an individual\u2019s decision-making process when selecting a qualified health plan in which to enroll; or (cc) to influence an enrollee\u2019s decision to stay enrolled in such plan; and (II) include or address content regarding the benefits, benefit structure, premiums, or cost sharing of such plan. (v) Termination The term termination , with respect to a contract or business arrangement between an agent or broker and a field marketing organization, third-party marketing organization, or health insurance issuer, means\u2014 (I) the ending of such contract or business arrangement, either unilaterally by one of the parties or on mutual agreement; or (II) the expiration of such contract or business arrangement that is not replaced by a substantially similar agreement. (vi) Third-party marketing organization The term third-party marketing organization means an organization or individual that is compensated to perform lead generation, marketing, or sales relating to enrollment of individuals in qualified health plans offered through an Exchange as part of the chain of enrollment. .\n##### (d) Transparency\nSection 1312(e) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18032(e) ) (as amended by subsection (c)) is amended by adding at the end the following:\n(2) Audits (A) In general For plan years beginning on or after such date specified by the Secretary, but not later than January 1, 2028, the Secretary, in coordination with the States and in consultation with the National Association of Insurance Commissioners, shall implement a process for the oversight and enforcement of agent and broker compliance with this section and other applicable Federal and State law (including regulations) that shall include\u2014 (i) periodic audits of agents and brokers based on\u2014 (I) complaints filed with the Secretary by individuals enrolled by such an agent or broker in a qualified health plan offered through an Exchange; (II) an incident or enrollment pattern that suggests fraud; and (III) other factors determined by the Secretary; and (ii) a process under which the Secretary shall share audit results and refer potential cases of fraud to the relevant State department of insurance. (B) Effect Nothing in this paragraph limits or restricts any referrals made under section 1311(i)(3) or any enforcement actions under section 1411(h). (3) List The Secretary shall develop a process to regularly provide to qualified health plans, Exchanges, and States a list of suspended and terminated agents and brokers. .",
      "versionDate": "2025-11-10",
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
        "actionDate": "2025-03-11",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "2079",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Insurance Fraud Accountability Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-11-06",
        "text": "Committee on Homeland Security and Governmental Affairs Senate Permanent Subcommittee on Investigations. Hearings held."
      },
      "number": "976",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Insurance Fraud Accountability Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-25",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1105",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No UPCODE Act",
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
        "updateDate": "2025-12-11T15:11:39Z"
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
      "date": "2025-11-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6010ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to extend and modify the enhanced premium tax credit, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T06:33:17Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to extend and modify the enhanced premium tax credit, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-11T09:05:30Z"
    }
  ]
}
```
