# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4409?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4409
- Title: START Act
- Congress: 119
- Bill type: S
- Bill number: 4409
- Origin chamber: Senate
- Introduced date: 2026-04-28
- Update date: 2026-05-21T16:58:47Z
- Update date including text: 2026-05-21T16:58:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in Senate
- 2026-04-28 - IntroReferral: Introduced in Senate
- 2026-04-28 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-04-28: Introduced in Senate

## Actions

- 2026-04-28 - IntroReferral: Introduced in Senate
- 2026-04-28 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4409",
    "number": "4409",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "START Act",
    "type": "S",
    "updateDate": "2026-05-21T16:58:47Z",
    "updateDateIncludingText": "2026-05-21T16:58:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-28",
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
      "actionDate": "2026-04-28",
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
          "date": "2026-04-28T20:14:49Z",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4409is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4409\nIN THE SENATE OF THE UNITED STATES\nApril 28, 2026 Mr. Banks (for himself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo clarify the program standards registration process for registered apprenticeship programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Streamlining Timely Apprenticeship Registration and Transparency Act or the START Act .\n#### 2. Apprenticeship program standards approval\nThe Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ) is amended\u2014\n**(1)**\nby redesignating section 4 as section 5; and\n**(2)**\nby inserting after section 3 the following:\n4. Apprenticeship program registration (a) Definitions For purposes of this section: (1) Competency-based approach (A) In general The term competency-based approach means, with respect to a program registered as an apprenticeship program under this Act, measuring skill acquisition in the program through the successful demonstration of acquired skills and knowledge, as verified by the program sponsor. (B) On-the-job learning A program described in subparagraph (A) program that uses the competency-based approach shall be required to include completion of an on-the-job learning component of the program for purposes of such an approach. (2) Complete program standards The term complete program standards means program standards submitted to the Secretary or a State apprenticeship agency in accordance with subsection (b)(1) that\u2014 (A) satisfy each of the requirements in subparagraphs (A) through (D) of such subsection; and (B) do not contain clerical errors as determined by the Secretary or State apprenticeship agency. (3) Incomplete program standards The term incomplete program standards means program standards submitted to the Secretary or a State apprenticeship agency in accordance with subsection (b)(1) that\u2014 (A) fail to satisfy one or more of the requirements in subparagraphs (A) through (D) of such subsection; or (B) contain clerical errors as determined by the Secretary or State apprenticeship agency. (4) National apprenticeship system The term national apprenticeship system means the system established by the Secretary of Labor to carry out the activities authorized and directed to be carried out under section 1. (5) Secretary The term Secretary means the Secretary of Labor. (6) State apprenticeship agency The term State apprenticeship agency means an entity of the government of a State that is recognized, under criteria established by the Secretary, for purposes of approving program standards that conform with the standards set by the Secretary for registering apprenticeship programs under the national apprenticeship system. (7) Time-based approach The term time-based approach means, with respect to a program registered as an apprenticeship program under this Act, measuring skill acquisition in the program through the completion of at least 2,000 hours of on-the-job learning as described in a work process schedule. (b) In general In administering this Act the Secretary shall establish a national apprenticeship system that provides the following: (1) Program standards for registration A person seeking to register a program as an apprenticeship program under this Act shall submit program standards to the Secretary or, as relevant, a State apprenticeship agency at such time and in such manner as the Secretary may require, that\u2014 (A) list each of the entities involved in the program, including any employer, group of employers, employer association, labor organization, or labor-management organization; (B) specify whether the program uses a competency-based, time-based, or hybrid approach; (C) provide sufficient information to determine whether the apprenticeship program standards conform with wage, safety, and licensing standards required by the State in which the program will operate and any other State standards with which the Secretary requires entities submitting program standards to comply; and (D) provide sufficient information to determine whether the apprenticeship program standards conform with standards of apprenticeship established by the Secretary under this Act, including the requirements under part 29 of title 29, Code of Federal Regulations (or successor regulations). (2) Reviewing program standards (A) In general Not later than 90 days after receipt by the Secretary or a State apprenticeship agency of program standards submitted in accordance with paragraph (1), the Secretary or State apprenticeship agency shall, if the program standards are complete program standards, provide to the prospective sponsor a decision that\u2014 (i) approves or denies the program standards; and (ii) if the decision is a denial, states the areas of noncompliance and provides suggestive action to correct the noncompliance. (B) Incomplete program standards Not later than 30 days after receipt by the Secretary or a State apprenticeship agency of program standards submitted in accordance with paragraph (1), the Secretary or State apprenticeship agency shall, if the program standards are incomplete program standards, provide the prospective sponsor with corrective feedback to direct the prospective sponsor to bring such program standards into conformity with complete program standards. (C) Performance accountability Beginning not later than 120 days after the date of enactment of this section, the Secretary shall, on a monthly basis, make publicly available online the average response times by the Secretary to standards submitted in accordance with paragraph (1), disaggregated by whether the standards are complete program standards or incomplete program standards. .\n#### 3. Clarification of the role of State apprenticeship councils\n##### (a) In general\nThe Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ), as amended by section 2, is further amended by adding at the end of section 4 of such Act (as added by section 2) the following:\n(3) State apprenticeship councils A State apprenticeship council of any State apprenticeship agency shall not\u2014 (A) have the final decision making authority for purposes of paragraph (2) over any program standards submitted in accordance with this subsection; or (B) be required to recommend any such program standards for purposes of such paragraph. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect on the date that is 2 years after the date of enactment of this Act.\n#### 4. Apprenticeship grant program\n##### (a) Definitions\nIn this section:\n**(1) Apprentice**\nThe term apprentice means an individual participating in a registered apprenticeship program.\n**(2) New apprentice**\nThe term new apprentice means, with respect to applying the formula established under subsection (c)(1) for a program year, an apprentice who is newly enrolled in a registered apprenticeship program in such program year.\n**(3) Program year**\nThe term program year means the year period beginning on July 1 and ending on June 30 of the next year.\n**(4) Registered apprenticeship program**\nThe term registered apprenticeship program means an apprenticeship program registered under the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ).\n**(5) Secretary**\nThe term Secretary means the Secretary of Labor.\n**(6) State**\nExcept in subsection (c)(1)(C), the term State means each of the several States of the United States, the District of Columbia, and any territory or possession of the United States.\n**(7) State apprenticeship agency**\nThe term State apprenticeship agency has the meaning given such term in section 4 of the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ).\n##### (b) In general\nFor each program year that begins after the date of enactment of this Act, the Secretary shall, not later than the beginning of the program year, award grants to States for the program year, in accordance with the formula under subsection (c), to carry out the activities described in subsection (d).\n##### (c) Award procedures\nThe Secretary shall award grant funds under subsection (b) in accordance with the following:\n**(1) Formula for allotment**\nNot later than 30 days before the start of each program year, the Secretary shall establish a formula to determine the allotment amounts for each program year for the grant that\u2014\n**(A)**\nis based on the population of the State and the number of apprentices whose primary residence is in the State as compared to the population of every other State and number of apprentices whose primary residence is in any other State;\n**(B)**\nis based on the number of new apprentices whose primary residence is in the State as compared to the number of new apprentices whose primary residence is in any other State; and\n**(C)**\nsubject to available appropriations, provides that each of the several States of the United States and the District of Columbia shall not be allotted less than $1,000,000 for each program year.\n**(2) Award amount**\nSubject to paragraph (3), the Secretary shall award each State an amount for a program year equal to the sum of\u2014\n**(A)**\nhalf of the amount allotted to the State under the formula established under paragraph (1) for the program year;\n**(B)**\nan amount (not more than the amount described in subparagraph (A)) equal to the matching amount in the notice submitted by the State under subsection (e); and\n**(C)**\nif the matching amount of the State is equal to the amount described in subparagraph (A), the proportional amount for the State as determined under paragraph (4).\n**(3) Deduction for delayed responses for registering apprenticeship programs**\n**(A) Determination of delay**\nThe Secretary shall determine the average complete program standards response time and the average incomplete program standards response time of each State that\u2014\n**(i)**\nreceives a grant under this section; and\n**(ii)**\nregisters registered apprenticeship programs in the State through a State apprenticeship agency.\n**(B) Deduction**\nFor each such State in which the Secretary under subparagraph (A) determines the average complete program standards response time is more than 90 days in a program year or the average incomplete program standards response time is more than 30 days in a program year, the Secretary shall deduct a percentage of the award amount under paragraph (2) for the next program year that is\u2014\n**(i)**\nequal to half of the sum of\u2014\n**(I)**\nthe number of days of the average complete program standards response time minus 90; and\n**(II)**\nthe number of days of the average incomplete program standards response time minus 30; but\n**(ii)**\nnot more than 20.\n**(C) Average response time**\n**(i) Definitions**\nFor purposes of this paragraph:\n**(I) Average complete program standards response time**\nThe term average complete program standards response time means the average number of days between the State receiving a complete program standards package by a program seeking to be a registered apprenticeship program and the State apprenticeship agency of the State providing an approval or a denial with suggestive action.\n**(II) Average incomplete program standards response time**\nThe term average incomplete program standards response time means the average number of days between the State receiving an incomplete program standards package by a program seeking to be a registered apprenticeship program and the State apprenticeship agency of the State providing a response with suggestive action.\n**(III) Complete program standards package; incomplete program standards package**\nThe terms complete program standards package and incomplete program standards package have the meanings given the terms complete program standards and incomplete program standards , respectively, in section 4 of the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ).\n**(IV) Suggestive action**\nThe term suggestive action means, with respect to program standards submitted by a program to a State apprenticeship agency to be a registered apprenticeship program, a response by the State apprenticeship agency to such program standards that is not an approval of the program standards and provides clear instructions to the sponsor of the program on how the program standards should be changed to conform with the requirements for registration as a registered apprenticeship program.\n**(ii) Rules of interpretation**\n**(I) Denial without suggestive action**\nFor purposes of determining average complete program standards response time, a denial without providing suggestive action shall not be interpreted to stop or pause the determination.\n**(II) Inquires on registration**\nFor purposes of determining average complete program standards response time and average incomplete program standards response time, an inquiry by a program to a State apprenticeship agency regarding the registration process that does not provide program standards documentation shall not be considered a submission of program standards.\n**(4) Proportional amount of allotted but unawarded funds**\n**(A) In general**\nNot less than 15 days before the start of each program year, the Secretary shall, for purposes of paragraph (2)(C), determine the proportional amount, as relevant, for each State that provides a matching amount under subsection (e) that is equal to the amount described in paragraph (2)(A) for the State for the program year.\n**(B) Proportional amount**\nThe proportional amount for a State for a program year is an amount that bears the same ratio to the amount of allotted but unawarded funds for the program year as the amount allotted to the State under the formula established under paragraph (1) for the program year bears to the total amount of funds allotted to all States under the formula for the program year.\n**(C) Allotted but unawarded funds**\nThe amount of allotted but unawarded funds for the program year is an amount equal to the total amount allotted under paragraph (1) for the program year minus the total amounts determined under subparagraphs (A) and (B) of paragraph (2) for all States for the program year.\n##### (d) Activities\nA State shall use amounts awarded under subsection (b) to\u2014\n**(1)**\nprovide technical assistance to existing and prospective sponsors of registered apprenticeship programs;\n**(2)**\nfund the training of apprentices, including by paying the wages of an apprentice;\n**(3)**\nfund outreach activities to increase awareness of registered apprenticeship programs and provide information on how to register an existing training program as a registered apprenticeship program; and\n**(4)**\nprovide financial incentives, including through pay-for-performance funding models, to attract employer investment in registered apprenticeship programs.\n##### (e) Notice of matching amount by States\n**(1) In general**\nNot less than 30 days before the start of each program year, a State seeking a grant under subsection (b) shall submit a notice to the Secretary of the amount the State intends to provide for the program year to match the amount provided through the grant, including proof of resources for the matching amount.\n**(2) Limit to matching amount**\nThe matching amount in a notice under paragraph (1) may not be more than half of the amount allotted to the State for the program year under the formula established under subsection (c)(1).\n##### (f) States without a State apprenticeship agency\nA State that does not have a State apprenticeship agency shall designate an agency of the State government for purposes of communications with the Secretary regarding the grant program under this section.\n##### (g) Authorization of appropriation\nThere is authorized to be appropriated to carry out the grant program under this section $150,000,000 for fiscal year 2027 and for each fiscal year thereafter.\n##### (h) Supplement not supplant\nFunds available for use under subsection (d) shall supplement and not supplant other State or local public funds expended that satisfy the activities under such subsection.\n#### 5. Posting reciprocity requirements\nThe Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ), as amended by sections 2 and 3, is further amended by adding at the end of section 4 of such Act (as added by section 2) the following:\n(4) Disclosure of reciprocity requirements Each State apprenticeship agency shall make publicly available online the process used by the State apprenticeship agency in the State of the agency for registering under this Act an apprenticeship program that has been otherwise registered under this Act by the Secretary or another State apprenticeship agency as a registered apprenticeship program in another State. .\n#### 6. Posting State apprenticeship standards\nThe Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ), as so amended, is further amended by adding at the end of section 4 of such Act (as added by section 2) the following:\n(5) Disclosure of State apprenticeship standards Each State apprenticeship agency shall make publicly available online information, as required by the Secretary, on apprenticeship standards in such State, including\u2014 (A) State minimum wage requirements; (B) State safety standards; and (C) instructions for properly completing documentation for proof of compliance with program standards pertaining to on-the-job training and related technical instruction requirements. .",
      "versionDate": "2026-04-28",
      "versionType": "Introduced in Senate"
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
        "name": "Labor and Employment",
        "updateDate": "2026-05-21T16:58:47Z"
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
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4409is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "START Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-13T04:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Streamlining Timely Apprenticeship Registration and Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-13T04:53:27Z"
    },
    {
      "title": "START Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T04:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to clarify the program standards registration process for registered apprenticeship programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-13T04:48:25Z"
    }
  ]
}
```
