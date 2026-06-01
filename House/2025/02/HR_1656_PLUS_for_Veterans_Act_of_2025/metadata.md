# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1656?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1656
- Title: PLUS for Veterans Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1656
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-04-10T16:57:43Z
- Update date including text: 2026-04-10T16:57:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-03 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-03 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1656",
    "number": "1656",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001301",
        "district": "1",
        "firstName": "Jack",
        "fullName": "Rep. Bergman, Jack [R-MI-1]",
        "lastName": "Bergman",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "PLUS for Veterans Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-10T16:57:43Z",
    "updateDateIncludingText": "2026-04-10T16:57:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-03",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-03T15:35:27Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "IA"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "NC"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "FL"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "NC"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "NC"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "MO"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "PA"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "GA"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "NC"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "NY"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "WI"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "NC"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "MO"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "FL"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "IA"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "TN"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "MI"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1656ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1656\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Bergman (for himself, Mr. Correa , Mrs. Miller-Meeks , Mr. Rouzer , Mr. Webster of Florida , Mr. McDowell , Mr. Harrigan , and Mr. Alford ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to permit certain fee agreements between claimants and agents or attorneys for the preparations, presentation, or prosecution of initial claims for benefits under the laws administered by the Secretary of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preserving Lawful Utilization of Services for Veterans Act of 2025 or the PLUS for Veterans Act of 2025 .\n#### 2. Clarification of preparation, presentation, or prosecution of a claim under a law administered by Secretary of Veterans Affairs\nSection 5901 of title 38, United States Code, is amended by adding at the end the following new subsection:\n(c) Exclusion The administration of a medical examination, or the completion of a report with respect to such medical examination, as described in section 5125 of this title, shall not constitute the preparation, presentation, or prosecution of a claim under the laws administered by the Secretary. .\n#### 3. Agents and attorneys in certain claims under laws administered by Secretary of Veterans Affairs: applications for recognition; fees allowable for representation; grounds for suspension; bars from recognition\n##### (a) In general\nSection 5904 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby inserting (A) before Except ; and\n**(ii)**\nby adding at the end the following new subparagraphs:\n(B) (i) An individual desiring recognition under this section shall submit to the Secretary an application, including an application submitted by mail, fax, or electronic means, in such form, at such time, and containing such information and assurances as the Secretary has determined appropriate to recognize such individual under this section. (ii) If the Secretary cannot verify whether the individual satisfies the qualifications and standards prescribed under paragraph (2) before the 90-day period beginning after the date on which the Secretary receives an application under clause (i), the Secretary shall recognize the individual on a conditional and temporary basis for a one-year period. (iii) At the end of such one-year period, the Secretary shall recognize the individual on a conditional and temporary basis for such additional one-year periods until the date on which the Secretary can verify whether the individual satisfies such qualifications and standards. (C) The Secretary may not suspend, exclude from further practice before the Department, fine pursuant to section 5905 of this title, or refuse to recognize as an agent or attorney under this section any individual on the basis that such individual, before the date of the enactment of this subparagraph\u2014 (i) charged a claimant a fee for services rendered in the preparation, presentation, or prosecution of an initial claim; or (ii) charged a claimant a fee for such services while such individual was not recognized under this section. ; and\n**(B)**\nby adding at the end the following new paragraph:\n(7) (A) The Secretary may charge and collect an assessment from an individual who\u2014 (i) seeks recognition under this section as an agent or attorney for the preparation, presentation, and prosecution of an initial claim under the laws administered by the Secretary; and (ii) charges or collects fees from a claimant for services rendered in such preparation, presentation, and prosecution. (B) An assessment described in subparagraph (A)\u2014 (i) shall be in such amount as the Secretary prescribes in regulations and determines appropriate; and (ii) may not exceed $500. (C) Amounts collected under this paragraph shall be deposited in a revolving fund in the Treasury of the United States. Such amounts shall be available to the Secretary for the administration of this section. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby redesignating paragraphs (1) through (9) as subparagraphs (A) through (I), respectively;\n**(B)**\nin the matter preceding subparagraph (A), as so redesignated, by inserting (1) before The Secretary ; and\n**(C)**\nin paragraph (1), as designated by paragraph (2)\u2014\n**(i)**\nin subparagraph (H), as so redesignated, by striking in accordance with subsection (c)(3)(A) ; or and inserting subsection (c)(2)(A) ;\n**(ii)**\nin subparagraph (I), as so redesignated, by striking the period at the end and inserting ; or ; and\n**(iii)**\nby adding at the end the following new subparagraph:\n(J) has failed to keep claimant data and personally identifiable information in accordance with applicable provisions of the Health Insurance Portability and Accountability Act of 1996 ( Public Law 104\u2013191 ; 42 U.S.C. 1301 et seq. ), including the data security requirements and implementing regulations of such Act. ; and\n**(D)**\nby adding at the end the following new paragraph:\n(2) Not later than one year after the date of the enactment of the Preserving Lawful Utilization of Services for Veterans Act of 2025 and annually thereafter, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report regarding the number of individuals suspended under this subsection or denied recognition under subsection (a), disaggregated by the reasons for such suspension or denial and whether the individual is\u2014 (A) a representative of an organization recognized under section 5902 of this title; (B) an agent; or (C) an attorney. ; and\n**(3)**\nin subsection (c)\u2014\n**(A)**\nby inserting Flat fee agreements.\u2014 after (c) ;\n**(B)**\nby striking paragraph (1) and inserting the following:\n(1) (A) In connection with a proceeding before the Department with respect to benefits under laws administered by the Secretary, a fee agreement between a claimant and an agent or attorney for the preparation, presentation, or prosecution of an initial claim for such benefits shall be a fee agreement described in subparagraph (B). (B) (i) A fee agreement described in this subparagraph is a fee agreement\u2014 (I) that does not require payment from a claimant to the agent or attorney before the date on which the claimant is provided notice of the agency of original jurisdiction's initial decision under section 5104 of this title with respect to the initial claim; (II) under which the total amount payable by the claimant to the agent or attorney with respect to the initial claim\u2014 (aa) is contingent on whether the initial claim is resolved in a manner favorable to the claimant; (bb) does not exceed the lesser of\u2014 (AA) $12,500 (as adjusted from time to time under subparagraph (C)); or (BB) the amount equal to the product of five and the amount of the monthly increase of benefits awarded to the claimant pursuant to the claim; and (III) that contains an attestation by the claimant that the agent or attorney provided to the claimant the standard form under clause (iii). (ii) For purposes of this subparagraph, an initial claim shall be considered to have been resolved in a manner favorable to the claimant if all or any part of the relief sought pursuant to the claim is granted. (iii) For use in fee agreements described in this subparagraph, the Secretary shall develop a standard form that includes the following notices: (I) That organizations recognized under section 5902 of this title furnish services with respect to initial claims under laws administered by the Secretary at no cost to claimants. (II) That a claimant may select a private physician for a medical examination described in section 5125 of this title regarding the initial claim. (III) That the agent or attorney with whom the claimant is entering such fee agreement may not refer the claimant to a private physician described in such section with whom the agent or attorney has a business relationship. (C) Effective on October 1 of each year (beginning in the first fiscal year after the date of the enactment of the Preserving Lawful Utilization of Services for Veterans Act of 2025 ), the Secretary shall increase the dollar amount in effect under clause (i) of subparagraph (B) by a percentage equal to the percentage by which the Consumer Price Index for all urban consumers (U.S. city average) increased during the 12-month period ending with the last month for which Consumer Price Index data is available. In the event that such Consumer Price Index does not increase during such period, the Secretary shall maintain the dollar amount in effect under such clause during the previous fiscal year. ; and\n**(C)**\nin paragraph (2)\u2014\n**(i)**\nby striking in a case referred to in paragraph (1) of this subsection ; and\n**(ii)**\nby inserting in a case after represents a person ;\n**(D)**\nin paragraph (3)(A), by striking paragraph (2) and inserting paragraph (1) or (2) .\n##### (b) Regulations\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall prescribe regulations to carry out the amendments made by this section.\n#### 4. Reinstatement of penalties for charging veterans unauthorized fees relating to claims under laws administered by the Secretary of Veterans Affairs\n##### (a) In general\nSection 5905 of title 38, United States Code, is amended\u2014\n**(1)**\nin the heading, by striking Penalty and inserting Penalties ;\n**(2)**\nby inserting (a) Withholding of benefits.\u2014 before Whoever ; and\n**(3)**\nby adding at the end the following new subsection:\n(b) Charging of unauthorized fees Except as provided in sections 5904 or 1984 of this title, whoever directly or indirectly solicits, contracts for, charges, or receives, or attempts to solicit, contract for, charge, or receive, any fee or compensation with respect to the preparation, presentation, or prosecution of any claim for benefits under the laws administered by the Secretary shall be fined as provided in title 18, or imprisoned not more than one year, or both. (c) Violations during conditional and temporary recognition If an individual recognized as an agent or attorney on a conditional and temporary basis pursuant to clause (ii) or (iii) of section 5904(a)(1)(B) of this title violates any law or regulation administered by the Secretary under this chapter on or after the date on which such individual is so recognized\u2014 (1) the Secretary shall, after notice, revoke the conditional and temporary recognition of the individual; and (2) such individual, after notice and opportunity for a hearing, shall be\u2014 (A) fined $50,000; and (B) barred from recognition under section 5904 of this title\u2014 (i) for a period of one year beginning on the date of the first violation; and (ii) for a period of 10 years beginning on the date of each subsequent violation. (d) Deposit of fines Any amount received by the Federal Government from a fine imposed under subsection (b) or (c) shall be deposited in the fund established by section 5904(a)(7)(C) of this title. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 59 of such title is amended by striking the item relating to section 5905 and inserting the following new item:\n5905. Penalties for certain acts. .\n##### (c) Effective date\nThe amendments made by this section shall take effect on the date that is 90 days after the date on which the Secretary prescribes the regulations required by subsection (b) of section 3.\n#### 5. Federal preemption\nThis Act, and the amendments made by this Act, supersede any State law that is inconsistent with the statutory rights established by this Act, or such amendments, and preclude the implementation of such a law, whether statutory, common law, or otherwise, and whether adopted before or after the date of enactment of this Act.",
      "versionDate": "2025-02-27",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-09-02T17:45:59Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-09-02T17:45:44Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-10T16:57:42Z"
          },
          {
            "name": "Federal preemption",
            "updateDate": "2025-09-02T17:46:10Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-09-02T17:45:39Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2025-09-02T17:46:04Z"
          },
          {
            "name": "Inflation and prices",
            "updateDate": "2025-09-02T17:45:54Z"
          },
          {
            "name": "Lawyers and legal services",
            "updateDate": "2025-09-02T17:45:35Z"
          },
          {
            "name": "Legal fees and court costs",
            "updateDate": "2025-09-02T17:45:24Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-09-02T17:45:50Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-09-02T17:45:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-25T17:59:54Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1656ih.xml"
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
      "title": "PLUS for Veterans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PLUS for Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preserving Lawful Utilization of Services for Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to permit certain fee agreements between claimants and agents or attorneys for the preparations, presentation, or prosecution of initial claims for benefits under the laws administered by the Secretary of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T09:18:26Z"
    }
  ]
}
```
