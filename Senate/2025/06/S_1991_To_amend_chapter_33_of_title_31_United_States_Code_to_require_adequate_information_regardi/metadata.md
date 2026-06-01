# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1991?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1991
- Title: Delivering On Government Efficiency in Spending Act
- Congress: 119
- Bill type: S
- Bill number: 1991
- Origin chamber: Senate
- Introduced date: 2025-06-09
- Update date: 2025-12-17T18:41:56Z
- Update date including text: 2025-12-17T18:41:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-09: Introduced in Senate
- 2025-06-09 - IntroReferral: Introduced in Senate
- 2025-06-09 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-12-10 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.
- Latest action: 2025-06-09: Introduced in Senate

## Actions

- 2025-06-09 - IntroReferral: Introduced in Senate
- 2025-06-09 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-12-10 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-09",
    "latestAction": {
      "actionDate": "2025-06-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1991",
    "number": "1991",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Delivering On Government Efficiency in Spending Act",
    "type": "S",
    "updateDate": "2025-12-17T18:41:56Z",
    "updateDateIncludingText": "2025-12-17T18:41:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-09",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-09",
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
          "date": "2025-12-10T19:30:02Z",
          "name": "Hearings By (full committee)"
        }
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-09T22:31:26Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "MT"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "WY"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "OK"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "UT"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "ID"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "AL"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "ND"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "KS"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "NC"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "MT"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "OK"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "AL"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "IA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "FL"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1991is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1991\nIN THE SENATE OF THE UNITED STATES\nJune 9, 2025 Ms. Ernst (for herself, Mr. Sheehy , Ms. Lummis , Mr. Mullin , Mr. Lee , Mr. Risch , Mr. Tuberville , Mr. Cramer , Mr. Marshall , Mr. Budd , Mr. Daines , Mr. Lankford , Mrs. Britt , Mr. Grassley , and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend chapter 33 of title 31, United States Code, to require adequate information regarding payments of Federal funds.\n#### 1. Short title\nThis Act may be cited as the Delivering On Government Efficiency in Spending Act .\n#### 2. Mandatory reporting and verification of payment information\n##### (a) In general\nSubchapter II of chapter 33 of title 31, United States Code is amended by adding at the end the following:\n3337. Mandatory reporting and verification of payment information (a) Definitions In this section: (1) Agency The term agency means\u2014 (A) an executive agency; (B) an independent regulatory agency, as defined in section 3502 of title 44; or (C) an entity that\u2014 (i) (I) is the Congress; (II) is a court of the United States; (III) is a government of a territory or possession of the United States; or (IV) is the District of Columbia; and (ii) uses a Treasury disbursement system. (2) Budget justification materials The term budget justification materials has the meaning given that term in section 3(b)(2)(A) of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note). (3) Secretary The term Secretary means the Secretary of the Treasury. (4) Sensitive operations The term sensitive operations \u2014 (A) means an operation of an agency related to a domestic law enforcement activity or the national security of the United States with respect to which the disclosure of information in accordance with subsection (b) would\u2014 (i) reasonably lead to death or serious bodily injury; or (ii) result in the disclosure of information\u2014 (I) the disclosure of which is prohibited by law; (II) that is classified; or (III) that is exempt from disclosure under section 552(b) of title 5; and (B) includes an operation described in subparagraph (A) that is carried out in tandem or coordination with, or in support of, a State, local, or Tribal government. (5) Treasury disbursement system The term Treasury disbursement system means any system operated by the Secretary for the purpose of disbursing public money. (b) Mandatory reporting of payment information Subject to subsection (e), for each payment authorized by the head of an agency that is submitted to a Treasury disbursement system for disbursement by the Secretary, the head of the agency shall provide to the Secretary, in such format as the Secretary requires, for inclusion in the Treasury disbursement system\u2014 (1) a brief description of the purpose for which the payment is being made; (2) the appropriations account (Treasury Account Symbol, or any successor thereto) from which the payment is to be drawn; and (3) the type of activity being reported (Business Event Type Code, or any successor thereto). (c) Periodic updates Not less frequently than once each fiscal year\u2014 (1) for each payment\u2014 (A) the certifying official shall evaluate whether the information collected under subsection (b) is accurate and complete; and (B) the head of each certifying agency shall provide written confirmation to the disbursing official attesting to the accuracy of such information; and (2) the disbursing official shall consult with the certifying official to improve the management of the Treasury disbursement system. (d) Public reporting Not later than 30 days after the date on which each payment that is subject to this subchapter is certified, the Director of the Office of Management and Budget shall direct the Secretary, or, if the payment is disbursed by an accountable official who is not in a position in the Department of the Treasury, the head of the agency with jurisdiction over the accountable official, to make available on the public website operated under the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note) the data required to be provided under subsection (b) with respect to the payment. (e) Exemptions Subsections (b), (c), and (d) shall not apply to a payment for which the head of the agency authorizing the payment verifies to the Secretary that the compliance with such subsections would adversely impact a sensitive operation for which the payment is authorized. (f) Report The head of each agency shall include in a controlled unclassified informational annex, or in a classified annex (if the applicable information has been properly classified by an officer or employee of the agency with original classification authority), as warranted, of the first budget justification materials of the agency submitted after the date of enactment of this section, and all budget justification materials submitted thereafter, a report that includes, for each payment that was made during the most recent prior fiscal year and for which the reporting of information was exempted under subsection (e), aggregated information which would have been provided to the Secretary under subsection (b), but for the exemption. .\n##### (b) Implementation\nThe Secretary of the Treasury may issue regulations or guidance to implement the amendments made by this Act.\n##### (c) Rule of construction\nNothing in this section, or an amendment made by this section, shall be construed to impose a legal liability on a disbursing official resulting from any action taken pursuant to this section, or an amendment made by this section.\n##### (d) Conforming amendment\nThe table of sections for chapter 33 of title 31, United States Code is amended by inserting after the item relating to section 3336 the following:\n3337. Mandatory reporting and verification of payment information. .\n#### 3. Data access for purposes of program integrity\n##### (a) Access to the National Directory of New Hires\nSection 453(j) of the Social Security Act ( 42 U.S.C. 653(j) ) is amended by adding at the end the following:\n(12) Information to assist in the prevention of improper payments (A) In general The Secretary of the Treasury shall have access to the information in the National Directory of New Hires for the purpose of identifying, preventing, and recovering improper payments. (B) Redisclosure For the purpose of identifying, preventing, and recovering improper payments, the Secretary of the Treasury may redisclose information in the National Directory of New Hires to\u2014 (i) agents and contractors of the Secretary of the Treasury; (ii) Federal and non-Federal agencies authorized to receive information in the National Directory of New Hires directly from the Secretary; and (iii) such additional persons and entities as agreed to by the Secretary and the Secretary of the Treasury. .\n##### (b) Bank account verification and precertification\nSection 3325 of title 31, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking the executive branch and inserting an agency ; and\n**(B)**\nin paragraph (1), by striking executive each place it appears;\n**(2)**\nin subsection (d), by striking executive each place it appears; and\n**(3)**\nby adding at the end the following:\n(e) (1) Prior to certifying a voucher to a disbursing official, the head of an agency or an officer or employee of an agency described in subparagraph (A) or (B) of subsection (a)(1), as applicable, shall take necessary actions to accurately disburse payments to the recipients of those payments, including by\u2014 (A) verifying the accuracy of the bank account information to which a payment is to be disbursed; and (B) comparing the bank account information of the proposed recipient to other payment records available to the agency. (2) The Secretary of the Treasury and, with the approval of the Secretary of the Treasury, the head of the agency having jurisdiction over a disbursing official, may issue guidance to carry out this subsection. (f) In this section, the term agency has the meaning given the term in section 3337 of this title. .\n##### (c) Access to information covered by FCRA\n**(1) Definitions**\nSection 603(k)(1) of the Fair Credit Reporting Act ( 15 U.S.C. 1681a(k)(1) ) is amended\u2014\n**(A)**\nin subparagraph (A), by striking and at the end;\n**(B)**\nin subparagraph (B), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(C) does not include\u2014 (i) any change to a Federal disbursement, including the pre-certification termination of such disbursement, that is\u2014 (I) based on a consumer report; and (II) made to improve the accuracy of the disbursement; or (ii) any action taken by an authorized user of the Working System of the Do Not Pay Initiative authorized by section 3354 of title 31, United States Code, in connection with the disbursement of a payment, as defined in section 3351 of that title, that is based on a consumer report. .\n**(2) Permissible uses of consumer reports**\nSection 604(a) of the Fair Credit Reporting Act ( 15 U.S.C. 1681b(a) ) is amended by adding at the end the following:\n(7) To the Secretary of the Treasury for purposes of assisting Federal and non-Federal entities identify, prevent, and recover improper payments, including redisclosing information in a consumer report to\u2014 (A) agents and contractors of the Department of the Treasury; and (B) Federal and non-Federal entities authorized to receive such information directly from the Secretary. .\n##### (d) Privacy-Preserving validation of select tax information\n**(1) In general**\nSection 6103(i) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(9) Do not pay working system (A) In general In response to an inquiry by the Secretary with respect to a specific individual, the Commissioner shall provide the Secretary with any return information described in subparagraph (B) with respect to such individual for the applicable period, in a manner which preserves the confidentiality of such information, for the purposes of enhancing the Do Not Pay working system described in section 3354(c) of title 31, United States Code, which may include disclosing such information\u2014 (i) to agents and contractors of the Department of Treasury who are authorized to access the Do Not Pay working system, and (ii) other Federal agencies and State agencies that manage Federally-funded State-administered programs (including agents and contractors of such agencies) who are authorized to access the Do Not Pay working system, for purposes of using the Do Not Pay working system to identify, prevent, and recover improper payments. (B) Return information The return information described in this subparagraph is the following: (i) Taxpayer identification number. (ii) Filing status. (iii) Adjusted gross income. (iv) Income or loss reported on Schedule C of Form 1040 (or successor forms). (v) Filing year. (vi) Bank account and routing information. (vii) Any reported identity theft related to the taxpayer identification number. (viii) Whether a tax return was not filed for any taxable year. (C) Applicable period For purposes of this paragraph, the term applicable period means, with respect to any individual, the period\u2014 (i) consisting of the number of taxable years specified by the Secretary in the inquiry made under subparagraph (A) (but not less than 3 taxable years), and (ii) ending with the most recently completed taxable year for which the information described in such subparagraph is available. .\n**(2) Effective date**\nThe amendment made by this section shall apply to disclosures made after the date of the enactment of this Act.\n##### (e) Access to Social Security information\nTitle II of the Social Security Act ( 42 U.S.C. 401 et seq. ) is amended by adding at the end the following new section:\n235. Disclosure of information for do not pay system (a) In general For the purposes described in subsection (b), the Commissioner of Social Security shall, upon request of the Secretary of the Treasury, enter into an agreement with the Department of the Treasury to regularly provide personally identifiable information held by the Social Security Administration, which shall, with respect to any individual, include, at a minimum, the name, date of birth, and Social Security number of such individual. (b) Purposes Information provided under subsection (a) shall be used solely for purposes of enhancing the Do Not Pay working system described in section 3354(c) of title 31, United States Code, with respect to identifying, preventing, and recovering improper payments, including fraudulent payments. .",
      "versionDate": "2025-06-09",
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
        "actionDate": "2025-07-10",
        "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committees on Ways and Means, and Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4311",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Delivering On Government Efficiency in Spending Act",
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
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2025-12-17T18:41:56Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-12-17T18:41:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-07-17T18:49:13Z"
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
      "date": "2025-06-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1991is.xml"
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
      "title": "Delivering On Government Efficiency in Spending Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Delivering On Government Efficiency in Spending Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-17T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend chapter 33 of title 31, United States Code, to require adequate information regarding payments of Federal funds.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-17T04:18:19Z"
    }
  ]
}
```
