# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1151?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1151
- Title: Accountability Through Electronic Verification Act
- Congress: 119
- Bill type: S
- Bill number: 1151
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2026-03-11T11:03:19Z
- Update date including text: 2026-03-11T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1151",
    "number": "1151",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Accountability Through Electronic Verification Act",
    "type": "S",
    "updateDate": "2026-03-11T11:03:19Z",
    "updateDateIncludingText": "2026-03-11T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-26",
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
        "item": [
          {
            "date": "2025-03-26T19:08:33Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-26T19:08:33Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "AL"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "UT"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "TX"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "AL"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "OK"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "WV"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "IA"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "OH"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "IN"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "TN"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "MT"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-03-10",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1151is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1151\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mr. Grassley (for himself, Mr. Tuberville , Mr. Lee , Mr. Cruz , Mrs. Britt , Mr. Lankford , Mrs. Capito , and Ms. Ernst ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo expand the use of E-Verify to hold employers accountable, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Accountability Through Electronic Verification Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Permanent reauthorization.\nSec. 3. Mandatory use of E-Verify.\nSec. 4. Consequences of failure to participate.\nSec. 5. Preemption; liability.\nSec. 6. Expanded use of E-Verify.\nSec. 7. Reverification.\nSec. 8. Holding employers accountable.\nSec. 9. Information sharing.\nSec. 10. Form I\u20139 process.\nSec. 11. Design and operation of E-Verify.\nSec. 12. Identity theft.\nSec. 13. Small Business Demonstration Program.\nSec. 14. Employer Compliance Inspection Center.\n#### 2. Permanent reauthorization\nSection 401(b) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 (division C of Public Law 104\u2013208 ; 8 U.S.C. 1324a note) is amended by striking Unless the Congress otherwise provides, the Secretary of Homeland Security shall terminate a pilot program on September 30, 2015. .\n#### 3. Mandatory use of E-Verify\n##### (a) Federal Government\nSection 402(e)(1) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 (division C of Public Law 104\u2013208 ; 8 U.S.C. 1324a note) is amended\u2014\n**(1)**\nby amending subparagraph (A) to read as follows:\n(A) Executive departments and agencies Each department and agency of the Federal Government shall participate in E-Verify by complying with the terms and conditions set forth in this section. ; and\n**(2)**\nin subparagraph (B), by striking , that conducts hiring in a State and all that follows and inserting shall participate in E-Verify by complying with the terms and conditions set forth in this section. .\n##### (b) Federal contractors; critical employers\nSection 402(e) of such Act, as amended by subsection (a), is further amended\u2014\n**(1)**\nby redesignating paragraphs (2) and (3) as paragraphs (4) and (5), respectively; and\n**(2)**\nby inserting after paragraph (1) the following:\n(2) United states contractors Any person, employer, or other entity that enters into a contract with the Federal Government shall participate in E-Verify by complying with the terms and conditions set forth in this section. (3) Designation of critical employers Not later than 7 days after the date of the enactment of the Accountability Through Electronic Verification Act , the Secretary of Homeland Security shall\u2014 (A) conduct an assessment of employers that are critical to the homeland security or national security needs of the United States; (B) designate and publish a list of employers and classes of employers that are deemed to be critical pursuant to the assessment conducted under subparagraph (A); and (C) require that critical employers designated pursuant to subparagraph (B) participate in E-Verify by complying with the terms and conditions set forth in this section not later than 30 days after the Secretary makes such designation. .\n##### (c) All employers\nSection 402 of such Act, as amended by this section, is further amended\u2014\n**(1)**\nby redesignating subsection (f) as subsection (h); and\n**(2)**\nby inserting after subsection (e) the following:\n(f) Mandatory participation in E-Verify (1) In general Subject to paragraphs (2) and (3), all employers in the United States shall participate in E-Verify, with respect to all employees recruited, referred, or hired by such employer on or after the date that is 1 year after the date of the enactment of the Accountability Through Electronic Verification Act . (2) Use of contract labor Any employer who uses a contract, subcontract, or exchange to obtain the labor of an individual in the United States shall certify in such contract, subcontract, or exchange that the employer, and all parties to such contract, subcontract, or exchange, use E-Verify. If such certification is not included in a contract, subcontract, or exchange, the employer shall be deemed to have violated paragraph (1). (3) Interim mandatory participation (A) In general Before the date set forth in paragraph (1), the Secretary of Homeland Security shall require any employer or class of employers to participate in E-Verify, with respect to all employees recruited, referred, or hired by such employer if the Secretary has reasonable cause to believe that such employer is or has been engaged in a material violation of section 274A of the Immigration and Nationality Act ( 8 U.S.C. 1324a ). (B) Notification Not later than 14 days before an employer or class of employers is required to begin participating in E-Verify pursuant to subparagraph (A), the Secretary shall provide such employer or class of employers with\u2014 (i) written notification of such requirement; and (ii) appropriate training materials to facilitate compliance with such requirement. .\n#### 4. Consequences of failure to participate\n##### (a) In general\nSection 402(e)(5) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1324a note), as redesignated by section 3(b)(1), is amended to read as follows:\n(5) Consequences of failure to participate If a person or other entity that is required to participate in E-Verify fails to comply with the requirements under this title with respect to an individual\u2014 (A) such failure shall be treated as a violation of section 274A(a)(1)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1324a ) with respect to such individual; and (B) a rebuttable presumption is created that the person or entity has violated section 274A(a)(1)(A) of such Act. .\n##### (b) Penalties\nSection 274A of the Immigration and Nationality Act ( 8 U.S.C. 1324a ) is amended\u2014\n**(1)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (4)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nin the matter preceding clause (i), by inserting , subject to paragraph (10), after in an amount ;\n**(II)**\nin clause (i), by striking not less than $250 and not more than $2,000 and inserting not less than $2,500 and not more than $5,000 ;\n**(III)**\nin clause (ii), by striking not less than $2,000 and not more than $5,000 and inserting not less than $5,000 and not more than $10,000 ; and\n**(IV)**\nin clause (iii), by striking not less than $3,000 and not more than $10,000 and inserting not less than $10,000 and not more than $25,000 ; and\n**(ii)**\nby amending subparagraph (B) to read as follows:\n(B) may require the person or entity to take such other remedial action as is appropriate. ;\n**(B)**\nin paragraph (5)\u2014\n**(i)**\nby striking of not less than $100 and not more than $1,000 and inserting , subject to paragraphs (10) through (12), of not less than $1,000 and not more than $25,000 ;\n**(ii)**\nby striking the size of the business of the employer being charged, the good faith of the employer and inserting the good faith of the employer being charged ; and\n**(iii)**\nby adding at the end the following: Failure by a person or entity to utilize the employment eligibility verification system as required by law, or providing information to the system that the person or entity knows or reasonably believes to be false, shall be treated as a violation of subsection (a)(1)(A). ; and\n**(C)**\nby adding at the end the following:\n(10) Exemption from penalty In the case of the imposition of a civil penalty under paragraph (4)(A) with respect to a violation of paragraph (1)(A) or (2) of subsection (a) for hiring, continuation of employment, recruitment, or referral by a person or entity and, in the case of the imposition of a civil penalty under paragraph (5) for a violation of subsection (a)(1)(B) for hiring, recruitment, or referral by a person or entity, the penalty otherwise imposed may be waived or reduced if the violator establishes that the violator acted in good faith. (11) Authority to debar employers for certain violations (A) In general If a person or entity is determined by the Secretary of Homeland Security to be a repeat violator of paragraph (1)(A) or (2) of subsection (a), or is convicted of a crime under this section, the Secretary of Homeland Security shall debar such person or entity from the receipt of Federal contracts, grants, or cooperative agreements in accordance with the debarment standards and pursuant to the debarment procedures set forth in the Federal Acquisition Regulation maintained under section 1303(a)(1) of title 41, United States Code. (B) Does not have contract, grant, agreement If the Secretary of Homeland Security debars a person or entity in accordance with this paragraph, and such person or entity does not hold a Federal contract, grant, or cooperative agreement, the Administrator of General Services shall include the person or entity on the List of Parties Excluded From Federal Procurement for 5 years. (C) Has contract, grant, agreement If the Secretary of Homeland Security debars a person or entity in accordance with this paragraph, and such person or entity holds a Federal contract, grant, or cooperative agreement, the Secretary\u2014 (i) shall notify all agencies or departments holding a contract, grant, or cooperative agreement with the debarred person or entity of such debarment; and (ii) after soliciting and considering the views of all such agencies and departments, may waive the operation of this paragraph. (D) Review Any decision to debar a person or entity under in accordance with this paragraph shall be reviewable pursuant to part 9.4 of the Federal Acquisition Regulation. ; and\n**(2)**\nin subsection (f)\u2014\n**(A)**\nby amending paragraph (1) to read as follows:\n(1) Criminal penalty Any person or entity which engages in a pattern or practice of violations of paragraph (1) or (2) of subsection (a) shall be fined not more than $30,000 for each unauthorized alien with respect to which such a violation occurs, imprisoned for not less than 1 year and not more than 10 years, or both, notwithstanding the provisions of any other Federal law relating to fine levels. ; and\n**(B)**\nin paragraph (2), by striking Attorney General each place such term appears and inserting Secretary of Homeland Security .\n#### 5. Preemption; liability\nSection 402 of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996, as amended by sections 3 and 4(a), is further amended by inserting after subsection (f) the following:\n(g) Limitation on State authority (1) Preemption A State or local government may not prohibit a person or other entity from verifying the employment authorization of new hires or current employees through E-Verify. (2) Liability A person or other entity that participates in E-Verify may not be held liable under any Federal, State, or local law for any employment-related action taken with respect to the wrongful termination of an individual in good faith reliance on information provided through E-Verify. .\n#### 6. Expanded use of E-Verify\nSection 403(a)(3)(A) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 (division C of Public Law 104\u2013208 ; 8 U.S.C. 1324a note) is amended to read as follows:\n(A) In general (i) Before hiring The person or other entity may verify the employment eligibility of an individual through E-Verify before the individual is hired, recruited, or referred if the individual consents to such verification. If an employer receives a tentative nonconfirmation for an individual, the employer shall comply with procedures prescribed by the Secretary of Homeland Security, including\u2014 (I) providing the individual employees with private, written notification of the finding and written referral instructions; (II) allowing the individual to contest the finding; and (III) not taking adverse action against the individual if the individual chooses to contest the finding. (ii) After employment offer The person or other entity shall verify the employment eligibility of an individual through E-Verify not later than 3 days after the date of the hiring, recruitment, or referral, as the case may be. (iii) Existing employees Not later than 1 year after the date of the enactment of the Accountability Through Electronic Verification Act , the Secretary shall require all employers to use E-Verify to verify the identity and employment eligibility of any individual who has not been previously verified by the employer through E-Verify. .\n#### 7. Reverification\nSection 403(a) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996, as amended by section 6, is further amended by adding at the end the following:\n(5) Reverification Each person or other entity participating in E-Verify shall use the E-Verify confirmation system to reverify the work authorization of any individual not later than 3 days after the date on which such individual\u2019s employment authorization is scheduled to expire (as indicated by the Secretary or the documents provided to the employer pursuant to section 274A(b) of the Immigration and Nationality Act ( 8 U.S.C. 1324a(b) )), in accordance with the procedures set forth in this subsection and in section 402. .\n#### 8. Holding employers accountable\n##### (a) Consequences of nonconfirmation\nSection 403(a)(4)(C) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 (division C of Public Law 104\u2013208 ; 8 U.S.C. 1324a note) is amended to read as follows:\n(C) Consequences of nonconfirmation (i) Termination and notification If the person or other entity receives a final nonconfirmation regarding an individual, the employer shall immediately\u2014 (I) terminate the employment, recruitment, or referral of the individual; and (II) submit to the Secretary any information relating to the individual that the Secretary determines would assist the Secretary in enforcing or administering United States immigration laws. (ii) Consequence of continued employment If the person or other entity continues to employ, recruit, or refer the individual after receiving final nonconfirmation, a rebuttable presumption is created that the employer has violated section 274A of the Immigration and Nationality Act ( 8 U.S.C. 1324a ). .\n##### (b) Interagency nonconfirmation report\nSection 405 of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 (division C of Public Law 104\u2013208 ; 8 U.S.C. 1324a note) is amended by adding at the end the following:\n(c) Interagency nonconfirmation report (1) In general The Director of U.S. Citizenship and Immigration Services shall submit a weekly report to the Director for U.S. Immigration and Customs Enforcement that includes, for each individual who receives final nonconfirmation through E-Verify\u2014 (A) the name of such individual; (B) his or her Social Security number or alien file number; (C) the name and contact information for his or her current employer; and (D) any other critical information that the Assistant Secretary determines to be appropriate. (2) Use of weekly report The Secretary of Homeland Security shall use information provided under paragraph (1) to enforce compliance with the United States immigration laws. .\n#### 9. Information sharing\nNot later than 1 year after the date of the enactment of this Act, the Commissioner of Social Security, the Commissioner of Internal Revenue, the Secretary of Homeland Security, and the Secretary of the Treasury shall jointly establish a program to share information among such agencies that may or could lead to the identification of unauthorized aliens (as defined in section 274A(h)(3) of the Immigration and Nationality Act ( 8 U.S.C. 1324a(h)(3) )), including no-match letters and any information in the earnings suspense file.\n#### 10. Form I\u20139 process\nNot later than 9 months after date of the enactment of this Act, the Secretary of Homeland Security shall submit a report to Congress that contains recommendations for\u2014\n**(1)**\nmodifying and simplifying the process by which employers are required to complete and retain a Form I\u20139 for each employee pursuant to section 274A of the Immigration and Nationality Act ( 8 U.S.C. 1324a ); and\n**(2)**\neliminating the process described in paragraph (1).\n#### 11. Design and operation of E-Verify\nSection 404(d) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 (division C of Public Law 104\u2013208 ; 8 U.S.C. 1324a note) is amended to read as follows:\n(d) Design and operation of system E-Verify shall be designed and operated\u2014 (1) to maximize its reliability and ease of use by employers; (2) to insulate and protect the privacy and security of the underlying information; (3) to maintain appropriate administrative, technical, and physical safeguards to prevent unauthorized disclosure of personal information; (4) to respond accurately to all inquiries made by employers on whether individuals are authorized to be employed; (5) to register any time when E-Verify is unable to receive inquiries; (6) to allow for auditing use of the system to detect fraud and identify theft; (7) to preserve the security of the information in all of the system by\u2014 (A) developing and using algorithms to detect potential identity theft, such as multiple uses of the same identifying information or documents; (B) developing and using algorithms to detect misuse of the system by employers and employees; (C) developing capabilities to detect anomalies in the use of the system that may indicate potential fraud or misuse of the system; and (D) auditing documents and information submitted by potential employees to employers, including authority to conduct interviews with employers and employees; (8) to confirm identity and work authorization through verification of records maintained by the Secretary, other Federal departments, States, the Commonwealth of the Northern Mariana Islands, or an outlying possession of the United States, as determined necessary by the Secretary, including\u2014 (A) records maintained by the Social Security Administration; (B) birth and death records maintained by vital statistics agencies of any State or other jurisdiction in the United States; (C) passport and visa records (including photographs) maintained by the Department of State; and (D) State driver's license or identity card information (including photographs) maintained by State department of motor vehicles; (9) to electronically confirm the issuance of the employment authorization or identity document; and (10) to display the digital photograph that the issuer placed on the document so that the employer can compare the photograph displayed to the photograph on the document presented by the employee or, in exceptional cases, if a photograph is not available from the issuer, to provide for a temporary alternative procedure, specified by the Secretary, for confirming the authenticity of the document. .\n#### 12. Identity theft\nSection 1028 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(7), by striking of another person and inserting that is not his or her own ; and\n**(2)**\nin subsection (b)(3)\u2014\n**(A)**\nin subparagraph (B), by striking or at the end;\n**(B)**\nin subparagraph (C), by adding or at the end; and\n**(C)**\nby adding at the end the following:\n(D) to facilitate or assist in harboring or hiring unauthorized workers in violation of section 274, 274A, or 274C of the Immigration and Nationality Act ( 8 U.S.C. 1324 , 1324a, and 1324c). .\n#### 13. Small Business Demonstration Program\nSection 403 of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996, as amended by section 6, 7, and 8, is further amended\u2014\n**(1)**\nby redesignating subsection (d) as subsection (e); and\n**(2)**\nby inserting after subsection (c) the following:\n(d) Small Business Demonstration Program Not later than 9 months after the date of the enactment of the Accountability Through Electronic Verification Act , the Director of U.S. Citizenship and Immigration Services shall establish a demonstration program that assists small businesses in rural areas or areas without internet capabilities to verify the employment eligibility of newly hired employees solely through the use of publicly accessible internet terminals. .\n#### 14. Employer Compliance Inspection Center\n##### (a) Establishment\nThere is established, within Homeland Security Investigations of U.S. Immigration and Customs Enforcement, the Employer Compliance Inspection Center (referred to in this section as the Center ).\n##### (b) Purposes\nThe purposes of the Center shall be\u2014\n**(1)**\nto create a culture of compliance for all United States businesses by imposing more effective, efficient, and standardized consequences, including civil and criminal penalties, on employers who fail to comply with the employment eligibility verification requirements; and\n**(2)**\nto consolidate worksite enforcement audits at a centralized location to ensure a standardized process and uniform application of the fine matrix.\n##### (c) Duties\nThe Center shall\u2014\n**(1)**\ncarry out duties related to the processing of the Employment Eligibility Verification Form I\u20139, including audits, and related worksite enforcement investigations;\n**(2)**\nensure that all United States businesses adhere to existing laws and regulations regarding employment eligibility; and\n**(3)**\ncarry out such additional duties as may be assigned or delegated by the Director of U.S. Immigration and Customs Enforcement.\n##### (d) Response time\nThe Center shall respond as quickly as practicable to employer inquiries based on the facts and circumstances of the employer making the inquiry.\n##### (e) Task force\nThe Center shall establish a task force, utilizing existing information sharing agreements with other Federal agencies, including the Social Security Administration, U.S. Citizenship and Immigration Services, the Department of Labor, and the Internal Revenue Service, to serve as a force multiplier to proactively investigate crimes, including Social Security fraud, tax fraud, and wage and hour violations.",
      "versionDate": "2025-03-26",
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
        "name": "Immigration",
        "updateDate": "2025-04-10T12:39:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-26",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s1151",
          "measure-number": "1151",
          "measure-type": "s",
          "orig-publish-date": "2025-03-26",
          "originChamber": "SENATE",
          "update-date": "2026-01-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1151v00",
            "update-date": "2026-01-22"
          },
          "action-date": "2025-03-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Accountability Through Electronic Verification Act</strong></p><p>This bill expands the E-Verify program by requiring all employers to use it and permanently reauthorizes the program. Currently, E-Verify use is voluntary for most employers, although some states mandate its use.</p><p>All employers must use E-Verify to confirm the identity and employment eligibility of all recruited, referred, or hired individuals, including current employees who were never verified under the program. Failure to use E-Verify shall create a rebuttable presumption that the employer is violating immigration law.</p><p>U.S. Citizenship and Immigration Services must generate weekly reports about individuals who have received a final nonconfirmation of employment eligibility. The Department of Homeland Security (DHS) must use the report to enforce immigration laws.</p><p>The bill increases civil and criminal penalties for hiring non-U.S. nationals (<em>aliens </em>under federal law) who are not authorized to work. DHS must bar repeat offenders and those criminally convicted from holding federal contracts, grants, or cooperative agreements.</p><p>The Social Security Administration, Internal Revenue Service, Department of the Treasury, and DHS must jointly establish a program to share information to help identify non-U.S. nationals who are not authorized to work.</p><p>The bill establishes the Employer Compliance Inspection Center within Homeland Security Investigations of U.S. Immigration and Customs Enforcement. The center's duties include processing I-9 employment eligibility verification forms and ensuring compliance with employment eligibility laws.</p><p>DHS must report to Congress on ways to simplify procedures relating to I-9 forms and on whether the I-9 process should be eliminated.</p>"
        },
        "title": "Accountability Through Electronic Verification Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1151.xml",
    "summary": {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Accountability Through Electronic Verification Act</strong></p><p>This bill expands the E-Verify program by requiring all employers to use it and permanently reauthorizes the program. Currently, E-Verify use is voluntary for most employers, although some states mandate its use.</p><p>All employers must use E-Verify to confirm the identity and employment eligibility of all recruited, referred, or hired individuals, including current employees who were never verified under the program. Failure to use E-Verify shall create a rebuttable presumption that the employer is violating immigration law.</p><p>U.S. Citizenship and Immigration Services must generate weekly reports about individuals who have received a final nonconfirmation of employment eligibility. The Department of Homeland Security (DHS) must use the report to enforce immigration laws.</p><p>The bill increases civil and criminal penalties for hiring non-U.S. nationals (<em>aliens </em>under federal law) who are not authorized to work. DHS must bar repeat offenders and those criminally convicted from holding federal contracts, grants, or cooperative agreements.</p><p>The Social Security Administration, Internal Revenue Service, Department of the Treasury, and DHS must jointly establish a program to share information to help identify non-U.S. nationals who are not authorized to work.</p><p>The bill establishes the Employer Compliance Inspection Center within Homeland Security Investigations of U.S. Immigration and Customs Enforcement. The center's duties include processing I-9 employment eligibility verification forms and ensuring compliance with employment eligibility laws.</p><p>DHS must report to Congress on ways to simplify procedures relating to I-9 forms and on whether the I-9 process should be eliminated.</p>",
      "updateDate": "2026-01-22",
      "versionCode": "id119s1151"
    },
    "title": "Accountability Through Electronic Verification Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Accountability Through Electronic Verification Act</strong></p><p>This bill expands the E-Verify program by requiring all employers to use it and permanently reauthorizes the program. Currently, E-Verify use is voluntary for most employers, although some states mandate its use.</p><p>All employers must use E-Verify to confirm the identity and employment eligibility of all recruited, referred, or hired individuals, including current employees who were never verified under the program. Failure to use E-Verify shall create a rebuttable presumption that the employer is violating immigration law.</p><p>U.S. Citizenship and Immigration Services must generate weekly reports about individuals who have received a final nonconfirmation of employment eligibility. The Department of Homeland Security (DHS) must use the report to enforce immigration laws.</p><p>The bill increases civil and criminal penalties for hiring non-U.S. nationals (<em>aliens </em>under federal law) who are not authorized to work. DHS must bar repeat offenders and those criminally convicted from holding federal contracts, grants, or cooperative agreements.</p><p>The Social Security Administration, Internal Revenue Service, Department of the Treasury, and DHS must jointly establish a program to share information to help identify non-U.S. nationals who are not authorized to work.</p><p>The bill establishes the Employer Compliance Inspection Center within Homeland Security Investigations of U.S. Immigration and Customs Enforcement. The center's duties include processing I-9 employment eligibility verification forms and ensuring compliance with employment eligibility laws.</p><p>DHS must report to Congress on ways to simplify procedures relating to I-9 forms and on whether the I-9 process should be eliminated.</p>",
      "updateDate": "2026-01-22",
      "versionCode": "id119s1151"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1151is.xml"
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
      "title": "Accountability Through Electronic Verification Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-11T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Accountability Through Electronic Verification Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to expand the use of E-Verify to hold employers accountable, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T01:48:34Z"
    }
  ]
}
```
