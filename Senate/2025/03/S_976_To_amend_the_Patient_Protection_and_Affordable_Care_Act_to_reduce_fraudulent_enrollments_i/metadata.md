# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/976?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/976
- Title: Insurance Fraud Accountability Act
- Congress: 119
- Bill type: S
- Bill number: 976
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2026-03-18T11:03:17Z
- Update date including text: 2026-03-18T11:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-11-06 - Committee: Committee on Homeland Security and Governmental Affairs Senate Permanent Subcommittee on Investigations. Hearings held.
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-11-06 - Committee: Committee on Homeland Security and Governmental Affairs Senate Permanent Subcommittee on Investigations. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/976",
    "number": "976",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Insurance Fraud Accountability Act",
    "type": "S",
    "updateDate": "2026-03-18T11:03:17Z",
    "updateDateIncludingText": "2026-03-18T11:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-06",
      "committees": {
        "item": {
          "name": "Permanent Subcommittee on Investigations",
          "systemCode": "ssga01"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Homeland Security and Governmental Affairs Senate Permanent Subcommittee on Investigations. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-12",
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
      "actionDate": "2025-03-12",
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
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-11-06T21:31:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-11-06T21:31:00Z",
                "name": "Hearings By (subcommittee)"
              }
            ]
          },
          "name": "Permanent Subcommittee on Investigations",
          "systemCode": "ssga01"
        }
      },
      "systemCode": "ssga00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-12T17:10:19Z",
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
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "IL"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "HI"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MN"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "WA"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "HI"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "NH"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MN"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "VT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MD"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "CT"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s976is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 976\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mr. Wyden (for himself, Ms. Duckworth , Ms. Hirono , Ms. Klobuchar , Mrs. Murray , Mr. Schatz , Mrs. Shaheen , Ms. Smith , Mr. Welch , and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Patient Protection and Affordable Care Act to reduce fraudulent enrollments in qualified health plans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Insurance Fraud Accountability Act .\n#### 2. Reduction of fraudulent enrollment in qualified health plans\n##### (a) Penalties for agents and brokers\nSection 1411(h)(1) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18081(h)(1) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nby redesignating clause (ii) as clause (iv);\n**(B)**\nin clause (i)\u2014\n**(i)**\nin the matter preceding subclause (I), by striking If\u2014 and all that follows through the such person in the matter following subclause (II) and inserting the following: If any person (other than an agent or broker) fails to provide correct information under subsection (b) and such failure is attributable to negligence or disregard of any rules or regulations of the Secretary, such person ; and\n**(ii)**\nin the second sentence, by striking For purposes and inserting the following:\n(iii) Definitions of negligence, disregard For purposes ;\n**(C)**\nby inserting after clause (i) the following:\n(ii) Civil penalties for certain violations by agents or brokers If any agent or broker fails to provide correct information under subsection (b) or section 1311(c)(8) or other information, as specified by the Secretary, and such failure is attributable to negligence or disregard of any rules or regulations of the Secretary, such agent or broker shall be subject, in addition to any other penalties that may be prescribed by law, including subparagraph (C), to a civil penalty of not less than $10,000 and not more than $50,000 with respect to each individual who is the subject of an application for which such incorrect information is provided. ; and\n**(D)**\nin clause (iv) (as so redesignated), by inserting or (ii) after clause (i) ;\n**(2)**\nin subparagraph (B)\u2014\n**(A)**\nby inserting including subparagraph (C), after law, ;\n**(B)**\nby striking Any person and inserting the following:\n(i) In general Any person ; and\n**(C)**\nby adding at the end the following:\n(ii) Civil penalties for knowing violations by agents or brokers (I) In general Any agent or broker who knowingly provides false or fraudulent information under subsection (b) or section 1311(c)(8), or other false or fraudulent information as part of an application for enrollment in a qualified health plan offered through an Exchange, as specified by the Secretary, shall be subject, in addition to any other penalties that may be prescribed by law, including subparagraph (C), to a civil penalty of not more than $200,000 with respect to each individual who is the subject of an application for which such false or fraudulent information is provided. (II) Procedure The provisions of section 1128A of the Social Security Act (other than subsections (a) and (b) of such section) shall apply to a civil monetary penalty under subclause (I) in the same manner as such provisions apply to a penalty or proceeding under section 1128A of the Social Security Act. ; and\n**(3)**\nby adding at the end the following:\n(C) Criminal penalties Any agent or broker who knowingly and willfully provides false or fraudulent information under subsection (b) or section 1311(c)(8), or other false or fraudulent information as part of an application for enrollment in a qualified health plan offered through an Exchange, as specified by the Secretary, shall be fined under title 18, United States Code, imprisoned for not more than 10 years, or both. .\n##### (b) Consumer protections\n**(1) In general**\nSection 1311(c) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18031(c) ) is amended by adding at the end the following:\n(8) Agent- or broker-assisted enrollment in qualified health plans in certain exchanges (A) In general For plan years beginning on or after such date specified by the Secretary, but not later than January 1, 2029, in the case of an Exchange that the Secretary operates pursuant to section 1321(c)(1), the Secretary shall establish a verification process for new enrollments of individuals in, and changes in coverage for individuals under, a qualified health plan offered through such Exchange, which are submitted by an agent or broker in accordance with section 1312(e) and for which the agent or broker is eligible to receive a commission. (B) Requirements The enrollment verification process under subparagraph (A) shall include\u2014 (i) a requirement that the agent or broker provide with the new enrollment or coverage change such documentation or evidence (such as a standardized consent form) or other sources as the Secretary determines necessary to establish that the agent or broker has the consent of the individual for the new enrollment or coverage change; (ii) a requirement that any commissions due to a broker or agent for such new enrollment or coverage change are paid after the enrollee has resolved all inconsistencies in accordance with paragraphs (3) and (4) of section 1411(e); (iii) a requirement that the information required under clause (i) and, as applicable, the date on which inconsistencies are resolved as described in clause (ii), is accessible to the applicable qualified health plan through a database or other resource, as determined by the Secretary, so that any commissions due to a broker or agent for such enrollment can be effectuated at the appropriate time; (iv) a requirement that individuals are notified of any changes to enrollment, coverage, the agent of record, or premium tax credits in a timely manner and that such notice provides plain language instructions on how individuals can cancel unauthorized activity; (v) a requirement that individuals be able to access their account information on a website or other technology platform, as defined by the Secretary, when used to submit an enrollment or plan change, in lieu of the Exchange website described in subsection (d)(4)(C), including information on the agent of record, the qualified health plan, and when any changes are made to the agent of record or the qualified health plan, on a consumer-facing website or through a toll-free telephone hotline; and (vi) a requirement that the agent or broker report to the Secretary any third-party marketing organization or field marketing organization (as such terms are defined in section 1312(e)) involved in the chain of enrollment (as so defined) with respect to such new enrollment or coverage change. (C) Consumer protection The Secretary shall ensure that the enrollment verification process under subparagraph (A) prioritizes continuity of coverage and care for individuals, including by not disenrolling individuals from a qualified health plan without the consent of the individual, regardless of whether the broker, agent, or qualified health plan is in violation of any requirement under this paragraph. .\n**(2) Required reporting**\nSection 1311(c)(1) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18031(c)(1) ) is amended\u2014\n**(A)**\nin subparagraph (H), by striking and at the end;\n**(B)**\nin subparagraph (I), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(J) report to the Secretary the termination (as defined in section 1312(e)(4)(C)) of an issuer. .\n##### (c) Authority To regulate field marketing organizations and third-Party marketing organizations\nSection 1312(e) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18032(e) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (1) and (2) as subclauses (I) and (II), respectively, and adjusting the margins accordingly;\n**(2)**\nin subclause (II) (as so redesignated), by striking the period at the end and inserting ; and ;\n**(3)**\nby striking the subsection designation and heading and all that follows through brokers\u2014 and inserting the following:\n(e) Regulation of agents, brokers, and certain marketing organizations (1) Agents, brokers, and certain marketing organizations (A) In general The Secretary shall establish procedures under which a State may allow\u2014 (i) agents or brokers\u2014 ; and\n**(4)**\nby adding at the end the following:\n(ii) field marketing organizations and third-party marketing organizations to participate in the chain of enrollment for an individual with respect to qualified health plans offered through an Exchange. (B) Criteria For plan years beginning on or after such date specified by the Secretary, but not later than January 1, 2029, the Secretary, by regulation, shall establish criteria for States to use in determining whether to allow agents and brokers to enroll individuals and employers in qualified health plans as described in subclause (I) of subparagraph (A)(i) and to assist individuals as described in subclause (II) of such subparagraph and field marketing organizations and third-party marketing organizations to participate in the chain of enrollment as described in subparagraph (A)(ii). Such criteria shall, at a minimum, require that\u2014 (i) an agent or broker act in accordance with a standard of conduct that includes a duty of such agent or broker to act in the best interests of the enrollee; (ii) a field marketing organization or third-party marketing organization agree to report the termination of an agent or broker to the applicable State and the Secretary, including the reason for termination; and (iii) an agent, broker, field marketing organization, or third-party marketing organization\u2014 (I) meet such marketing requirements as are required by the Secretary; (II) meet marketing requirements in accordance with other applicable Federal or State law; (III) does not employ practices that are confusing or misleading, as determined by the Secretary; (IV) submit all marketing materials to the Secretary for, as determined appropriate by the Secretary, review and approval; (V) is a licensed agent or broker or meets other licensure requirements, as required by the State; (VI) register with the Secretary; and (VII) does not compensate any individual or organization for referrals or any other service relating to the sale of, marketing for, or enrollment in qualified health plans unless such individual or organization meets the criteria described in subclauses (I) through (VI). (C) Definitions In this paragraph: (i) Chain of enrollment The term chain of enrollment , with respect to enrollment of an individual in a qualified health plan offered through an Exchange, means any steps taken from marketing to such individual, to such individual making an enrollment decision with respect to such a plan. (ii) Field marketing organization The term field marketing organization means an organization or individual that directly employs or contracts with agents and brokers, or contracts with carriers, to provide functions relating to enrollment of individuals in qualified health plans offered through an Exchange as part of the chain of enrollment. (iii) Marketing The term marketing means the use of marketing materials to provide information to current and prospective enrollees in a qualified health plan offered through an Exchange. (iv) Marketing materials The term marketing materials means materials relating to a qualified health plan offered through an Exchange or benefits offered through an Exchange that\u2014 (I) are intended\u2014 (aa) to draw an individual\u2019s attention to such plan or the premium tax credits or cost-sharing reductions for such plan or plans offered through an Exchange; (bb) to influence an individual\u2019s decision-making process when selecting a qualified health plan in which to enroll; or (cc) to influence an enrollee\u2019s decision to stay enrolled in such plan; and (II) include or address content regarding the benefits, benefit structure, premiums, or cost sharing of such plan. (v) Termination The term termination , with respect to a contract or business arrangement between an agent or broker and a field marketing organization, third-party marketing organization, or health insurance issuer, means\u2014 (I) the ending of such contract or business arrangement, either unilaterally by one of the parties or on mutual agreement; or (II) the expiration of such contract or business arrangement that is not replaced by a substantially similar agreement. (vi) Third-party marketing organization The term third-party marketing organization means an organization or individual that is compensated to perform lead generation, marketing, or sales relating to enrollment of individuals in qualified health plans offered through an Exchange as part of the chain of enrollment. .\n##### (d) Transparency\nSection 1312(e) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18032(e) ) (as amended by subsection (c)) is amended by adding at the end the following:\n(2) Audits (A) In general For plan years beginning on or after such date specified by the Secretary, but not later than January 1, 2029, the Secretary, in coordination with the States and in consultation with the National Association of Insurance Commissioners, shall implement a process for the oversight and enforcement of agent and broker compliance with this section and other applicable Federal and State law (including regulations) that shall include\u2014 (i) periodic audits of agents and brokers based on\u2014 (I) complaints filed with the Secretary by individuals enrolled by such an agent or broker in a qualified health plan offered through an Exchange; (II) an incident or enrollment pattern that suggests fraud; and (III) other factors determined by the Secretary; and (ii) a process under which the Secretary shall share audit results and refer potential cases of fraud to the relevant State department of insurance. (B) Effect Nothing in this paragraph limits or restricts any referrals made under section 1311(i)(3) or any enforcement actions under section 1411(h) . (3) List The Secretary shall develop a process to regularly provide to qualified health plans, Exchanges, and States a list of suspended and terminated agents and brokers. .",
      "versionDate": "2025-03-12",
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
        "actionDate": "2025-11-10",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6010",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend the Internal Revenue Code of 1986 to extend and modify the enhanced premium tax credit, and for other purposes.",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-10",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, and Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6575",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "CommonGround for Affordable Health Care Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-09",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6501",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Insurance Affordability Act",
      "type": "HR"
    },
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
          "type": "Identical bill"
        }
      },
      "title": "Insurance Fraud Accountability Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Accounting and auditing",
            "updateDate": "2025-11-17T18:30:42Z"
          },
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-11-17T18:30:35Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-11-17T18:30:18Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2025-11-17T18:30:27Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-11-17T18:30:22Z"
          },
          {
            "name": "Department of Health and Human Services",
            "updateDate": "2025-11-17T18:30:39Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-11-17T18:30:10Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-11-17T18:30:46Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-11-17T18:30:14Z"
          },
          {
            "name": "Marketing and advertising",
            "updateDate": "2025-11-17T18:30:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-04-04T13:41:27Z"
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
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s976is.xml"
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
      "title": "Insurance Fraud Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Patient Protection and Affordable Care Act to reduce fraudulent enrollments in qualified health plans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Insurance Fraud Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:20Z"
    }
  ]
}
```
