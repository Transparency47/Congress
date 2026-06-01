# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6323?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6323
- Title: Taxpayer Protection and Preparer Proficiency Act
- Congress: 119
- Bill type: HR
- Bill number: 6323
- Origin chamber: House
- Introduced date: 2025-11-28
- Update date: 2026-05-08T08:06:45Z
- Update date including text: 2026-05-08T08:06:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-28: Introduced in House
- 2025-11-28 - IntroReferral: Introduced in House
- 2025-11-28 - IntroReferral: Introduced in House
- 2025-11-28 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-11-28: Introduced in House

## Actions

- 2025-11-28 - IntroReferral: Introduced in House
- 2025-11-28 - IntroReferral: Introduced in House
- 2025-11-28 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-28",
    "latestAction": {
      "actionDate": "2025-11-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6323",
    "number": "6323",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "P000613",
        "district": "19",
        "firstName": "Jimmy",
        "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
        "lastName": "Panetta",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Taxpayer Protection and Preparer Proficiency Act",
    "type": "HR",
    "updateDate": "2026-05-08T08:06:45Z",
    "updateDateIncludingText": "2026-05-08T08:06:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-28",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-28",
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
          "date": "2025-11-28T15:00:10Z",
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
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-11-28",
      "state": "FL"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "AL"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6323ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6323\nIN THE HOUSE OF REPRESENTATIVES\nNovember 28, 2025 Mr. Panetta (for himself and Mr. Steube ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to penalize improper compliance with certain taxpayer requirements, and for other purposes.\n#### 1. Short title; etc\n##### (a) Short title\nThis Act may be cited as the Taxpayer Protection and Preparer Proficiency Act .\n##### (b) References to Internal Revenue Code\nExcept as otherwise expressly provided, whenever in this Act an amendment is expressed in terms of an amendment to a section or other provision, the reference shall be considered to be made to a section or other provision of the Internal Revenue Code of 1986.\n##### (c) References to Secretary\nFor purposes of this Act, the term Secretary means the Secretary of the Treasury or the Secretary's delegate.\n#### 2. Penalties for tax return preparers who improperly alter returns\n##### (a) In general\nParagraph (1) of section 6696(e) is amended to read as follows:\n(1) Return The term return means\u2014 (A) any return of any tax imposed by this title, (B) any administrative adjustment request under section 6227, (C) any partnership adjustment tracking report under section 6226(b)(4)(A), and (D) any other document purporting to be a return, request, or report described in subparagraphs (A) through (C). .\n##### (b) Effective date\nThe amendment made by this section shall take effect on the date of enactment of this Act.\n#### 3. Penalties for invalid or appropriated preparer identification numbers\n##### (a) In general\nSection 6695 is amended\u2014\n**(1)**\nby striking subsection (c) and inserting the following:\n(c) Failure To furnish valid identifying number (1) In general (A) Penalty Any person who is a tax return preparer with respect to any return or claim for refund and who fails to furnish an identifying number which complies with section 6109(a)(4)(A) with respect to such return or claim shall pay a penalty of $250 for such failure. (B) Non-compliance For purposes of this paragraph, an identifying number shall be deemed to not comply with section 6109(a)(4)(A) if such identifying number\u2014 (i) is assigned to another person, (ii) does not exist, (iii) is inactive or expired, (iv) has been withdrawn, (v) is suspended or has been revoked, or (vi) is otherwise invalid for use by the tax return preparer. (2) Exception The penalty imposed under paragraph (1) shall not apply if it is shown that such failure is due to reasonable cause and not due to willful neglect. (3) Limitation The maximum penalty imposed under this subsection on any person with respect to documents filed during any calendar year shall not exceed $75,000. ,\n**(2)**\nby redesignating subsection (h) as subsection (i),\n**(3)**\nby inserting after subsection (g) the following new subsection:\n(h) Use of invalid or appropriated electronic filing identification number (1) In general Any person who is an electronic return originator with respect to any return or claim for refund who fails to use, with respect to such return or claim, an electronic filing identification number which is assigned to such person by the Secretary, shall pay a penalty of $250 for such failure, unless it is shown that such failure is due to reasonable cause and not due to willful neglect. (2) Definitions For purposes of this subsection\u2014 (A) Electronic return originator (i) In general The term electronic return originator means a person who originates the electronic submission of 1 or more returns or claims for refund on behalf of other taxpayers. (ii) Exceptions The term electronic return originator shall not include a person merely because such person originates an electronic submission described in clause (i)\u2014 (I) by furnishing mechanical assistance to a person described in such subclause, (II) at the direction of an employer (or of an officer or employee of the employer) by whom such person is regularly and continuously employed, (III) as a fiduciary, or (IV) in response to a determination that directly or indirectly affects the tax liability of a taxpayer. (B) Electronic filing identification number (i) In general The term electronic filing identification number means an identification number assigned by the Secretary to a person authorized to file returns in electronic format on behalf of other taxpayers. (ii) Suspension or revocation In the case of any electronic filing identification number which has been suspended or revoked by the Secretary, such number shall not be deemed valid for purposes of paragraph (1). , and\n**(4)**\nin subsection (i)(1), as redesignated by paragraph (2), by striking and (g) and inserting (g), and (h) .\n##### (b) Modification of definition of tax return preparer\nSection 7701(a)(36) is amended\u2014\n**(1)**\nby striking subparagraph (A) and inserting the following:\n(A) In general The term tax return preparer means any person who prepares for compensation, or who employs one or more persons to prepare for compensation, any return of tax imposed by this title, any document purporting to be a return of tax imposed by this title, or any claim for refund of tax imposed by this title. For purposes of the preceding sentence, the preparation of a substantial portion of a return, document purporting to be a return, or claim for refund shall be treated as if it were the preparation of such return, document purporting to be a return, or claim for refund. , and\n**(2)**\nin subparagraph (B)\u2014\n**(A)**\nin clause (ii), by striking return or claim for refund and inserting return, document purporting to be a return, or claim for refund , and\n**(B)**\nin clause (iii), by striking return or claim for refund and inserting return, document purporting to be a return, or claim for refund .\n##### (c) Prevention of inadvertent errors involving identifying numbers\n**(1) In general**\nNot later than 18 months after the date of enactment of this Act, the Secretary shall establish a program to improve voluntary compliance with respect to requirements under subsections (c) and (h) of section 6695 of the Internal Revenue Code of 1986 (as amended by this section) and avoid the imposition of penalties under such subsections.\n**(2) Opportunity to correct**\nFor purposes of the program described in paragraph (1), the Secretary shall\u2014\n**(A)**\nprior to acceptance for processing, identify\u2014\n**(i)**\nany return or claim for refund which has been electronically submitted and does not include an identifying number which complies with section 6109(a)(4)(A) of the Internal Revenue Code of 1986, and\n**(ii)**\nany return or claim for refund which has been electronically submitted and does not include an electronic filing identification number (as defined in section 6695(h)(2)(B) of such Code), and\n**(B)**\nprovide an opportunity for the person who submitted such return or claim for refund to avoid imposition of a penalty under subsection (c) or (h) of section 6695 of such Code, as applicable, if\u2014\n**(i)**\nsuch return or claim for refund is withdrawn, or\n**(ii)**\nthe correct identifying number or electronic filing identification number is provided.\n##### (d) Criminal penalty\n**(1) In general**\nPart I of subchapter A of chapter 75 is amended by adding at the end the following new section:\n7218. Willful misuse or misappropriation of identifying number (a) In general Any tax return preparer who, with respect to any return, document purporting to be a return, or claim for refund\u2014 (1) willfully fails to furnish a valid preparer tax identification number with intent to evade or defeat the application of any requirement under any provision of this title which requires such preparer to obtain and furnish such number, (2) willfully furnishes a preparer tax identification number which\u2014 (A) does not exist, (B) is inactive or expired, (C) has been withdrawn, (D) is suspended or has been revoked, or (E) is otherwise invalid for use by such tax return preparer, or (3) willfully furnishes a preparer tax identification number which is assigned to another person, shall, in addition to any other penalties provided by law, be guilty of a felony and, upon conviction thereof, shall be fined not more than $50,000 ($100,000 in the case of a corporation), or imprisoned not more than 2 years, or both, together with the costs of prosecution. (b) Preparer tax identification number The term preparer tax identification number means an identifying number described in section 6109(a)(4)(A). .\n**(2) Clerical amendment**\nThe table of sections for part I of subchapter A of chapter 75 is amended by adding at the end the following new item:\nSec. 7218. Willful misuse or misappropriation of identifying number. .\n##### (e) Effective date\nThe amendments made by this section shall apply to returns or claims for refund filed after the date which is 18 months after the date of enactment of this Act.\n#### 4. Penalties for improper tax preparation or misappropriation of refunds\n##### (a) Other assessable penalties with respect to the preparation of tax returns for other persons\nSection 6695 , as amended by the preceding provisions of this Act, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking $50 and inserting $250 , and\n**(B)**\nby striking $25,000 and inserting $50,000 ,\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby striking $50 and inserting $250 , and\n**(B)**\nby striking $25,000 and inserting $75,000 ,\n**(3)**\nin subsection (d)\u2014\n**(A)**\nby striking $50 and inserting $250 , and\n**(B)**\nby striking $25,000 and inserting $50,000 ,\n**(4)**\nin subsection (e)\u2014\n**(A)**\nby striking $50 and inserting $250 , and\n**(B)**\nby striking $25,000 and inserting $75,000 ,\n**(5)**\nin subsection (g), by striking $500 and inserting $1,000 , and\n**(6)**\nin subsection (i)(1)\u2014\n**(A)**\nby striking 2014 and inserting 2024 , and\n**(B)**\nby striking calendar year 2013 and inserting calendar year 2023 .\n##### (b) Misappropriation of electronic funds transfer\n**(1) In general**\nSubsection (f) of section 6695 is amended to read as follows:\n(f) Negotiation of check; misappropriation (1) In general Any person who is a tax return preparer who\u2014 (A) endorses or otherwise negotiates (directly or through an agent) any check made in respect of the taxes imposed by this title which is issued to a taxpayer (other than the tax return preparer), or (B) misappropriates any refund (or advance payment with respect to a refundable credit), or any portion thereof, issued to any taxpayer through an electronic funds transfer, shall pay a penalty in an amount determined under paragraph (2). (2) Penalty The amount of the penalty determined under this paragraph shall, with respect to each check or transfer described in paragraph (1), be equal to the greater of\u2014 (A) $1,000, or (B) the full amount of such check or transfer. (3) Exception Paragraph (1)(A) shall not apply with respect to the deposit by a bank (within the meaning of section 581) of the full amount of the check in the taxpayer's account in such bank for the benefit of the taxpayer. .\n**(2) Conforming amendment**\nSection 6695(i)(1) is amended by striking (f), and inserting (f)(2)(A), .\n#### 5. Authority to deny, revoke, or suspend preparer tax identification numbers\n##### (a) In general\nSection 6109 is amended\u2014\n**(1)**\nin subsection (a), by striking paragraph (4) and inserting the following:\n(4) Furnishing identifying number of tax return preparer (A) In general Any return or claim for refund which is prepared by a tax return preparer shall bear such identifying number for securing proper identification of such preparer, their employer, or both, as may be prescribed. (B) Exception for supervised preparer Subparagraph (A) shall not apply with respect to any tax return preparer who prepares any return or claim for refund if such preparer is\u2014 (i) employed by a specified practitioner, and (ii) under the supervision and direction of a tax return preparer who\u2014 (I) includes their identifying number (as described in subparagraph (A)) on such return or claim, (II) signs such return or claim, and (III) is a specified practitioner. (C) Suspension or revocation In the case of any identifying number which has been suspended or revoked by the Secretary under subsection (e), such number shall not be deemed valid for purposes of subparagraph (A). (D) Definitions For purposes of this section\u2014 (i) Specified practitioner The term specified practitioner means a certified public accountant, attorney, or enrolled agent\u2014 (I) who is in good standing and authorized to represent persons before the Department of the Treasury under section 330 of title 31, United States Code, and (II) whose professional license or certification has not been revoked. (ii) Return; claim for refund The terms return and claim for refund have the respective meanings given to such terms by section 6696(e). , and\n**(2)**\nby inserting after subsection (d) the following:\n(e) Identifying number of tax return preparer (1) In general The Secretary shall maintain a program for administration of preparer tax identification numbers required under subsection (a)(4), which shall include restrictions on the issuance of such numbers to any individual other than an individual who\u2014 (A) meets the suitability requirements of paragraph (2) and the education requirements of paragraph (3), (B) meets the state program requirements of paragraph (4), or (C) is a specified practitioner. (2) Demonstration of suitability (A) In general An individual meets the suitability requirements of this paragraph if such individual has demonstrated to the Secretary the individual's suitability to be a tax return preparer by\u2014 (i) providing such information as the Secretary determines necessary, and (ii) undergoing a background check, including a review by the Secretary regarding compliance with personal tax obligations. (B) Conduct demonstrating lack of suitability For purposes of subparagraph (A), an individual shall be deemed to have failed to demonstrate their suitability to be a tax return preparer if\u2014 (i) any license or registration issued to such individual by a State to prepare tax returns has been suspended or revoked by such State, or (ii) the Secretary determines that such individual is described in clauses (ii) through (vi) of paragraph (5)(A). (C) Regulations and guidance The Secretary shall issue such regulations or other guidance as the Secretary determines necessary to carry out the purposes of this paragraph. (D) Prohibition on examinations For purposes of subparagraph (A), except as provided in paragraph (3)(C)(iii), the Secretary may not require an examination as a prerequisite for the assignment or renewal of a preparer tax identification number. (E) Grandfathering of prior background checks For purposes of subparagraph (A)(ii), in the case of an individual who has undergone a background check prior to the date of enactment of this subsection, the Secretary may deem such individual to have satisfied the requirement under such subparagraph. (3) Educational programs (A) In general An individual meets the education requirements of this paragraph if such individual completes a specified number of hours of educational programs on ethics, professional responsibility, and tax law (including recently enacted legislation) as may be required by the Secretary prior to the assignment or renewal of a preparer tax identification number. (B) Additional educational requirements for renewal The Secretary may require any individual seeking the renewal of a preparer tax identification number to complete educational programs in addition to those required under subparagraph (A). Any educational programs required under this subparagraph shall be based on\u2014 (i) a review of returns which include the preparer tax identification number of such preparer, and (ii) any errors identified by the Secretary as part of the review described in clause (i). (C) Other requirements For purposes of this paragraph, the Secretary\u2014 (i) may not require a tax return preparer to annually complete more than 18 hours of educational programs, (ii) shall require that any educational program include written materials which satisfy such standards as are established by the Secretary, (iii) may require that any educational program include a method to ensure that the tax return preparer attended the program and sufficiently understood the material presented, and (iv) may not direct any educational program to be completed through a specific provider. (D) Notice of failure to timely complete requirements The Secretary shall provide any tax return preparer who fails to complete the requirements of this paragraph notice of such failure and a period in which to cure such failure. (E) Publication of approved courses The Secretary shall publish, on the public website of the Internal Revenue Service\u2014 (i) a list of educational programs which have been determined by the Secretary to satisfy the requirement under clause (ii) of subparagraph (C) (and, if applicable, the requirement under clause (iii) of such subparagraph), including the providers of such programs, and (ii) any such requirements as the Secretary deems necessary to impose with respect to any additional programs required under subparagraph (B). (4) Exemption (A) In general Subject to subparagraph (B), any individual meets the state program requirements of this paragraph if such individual maintains a valid State license or registration issued by a State licensing program or State registration program (including State tax education councils) which includes examination, education, and background check requirements that are determined by the Secretary (on the basis of such information as is provided by the taxpayer or State program) to be comparable to the suitability requirements described in paragraph (2) and the education requirements described in paragraph (3). (B) Grandfathering of certain programs For purposes of subparagraph (A), with respect to determining whether a State licensing program or State registration program (including State tax education councils) includes examination, education, and background check requirements which are comparable to the suitability requirements described in paragraph (2) and the education requirements described in paragraph (3), such determination shall be made by the Secretary without regard to whether such requirements were included in such program at the time that such individual was licensed or registered under such program, provided that such requirements are, as of the date that such individual requested assignment or renewal of a preparer tax identification number under this subsection, presently included in such program. (5) Authority to revoke or suspend preparer tax identification number (A) In general The Secretary may suspend or revoke a preparer tax identification number if, after notice and opportunity for a hearing, the Secretary makes a determination that the tax return preparer\u2014 (i) has not met\u2014 (I) the suitability requirements of paragraph (2) and the education requirements of paragraph (3), or (II) the State program requirements of paragraph (4), (ii) is incompetent, as demonstrated by a repeated pattern of errors in returns that were prepared by such preparer or individuals who were supervised by such preparer (as described in subsection (a)(4)(B)) which affected the determination of tax liability in such returns, (iii) is disreputable, as demonstrated by\u2014 (I) giving false or misleading information under paragraph (2)(A)(i), (II) failure to comply with personal tax obligations, (III) revocation or suspension of any license or registration issued by a State for the preparation of tax returns, (IV) conviction of any criminal offense\u2014 (aa) involving dishonesty or breach of trust, or (bb) which is punishable under this title, (V) a final determination of liability for a penalty pursuant to section 6694, 6695(h), 6700, 6701, or 6702, or (VI) any conduct similar to the conduct described in subclauses (I) through (V), (iv) in the case of a person subject to regulation under section 330 of title 31, United States Code, or regulations prescribed thereunder, has violated the requirements under such section or such regulations, (v) with intent to defraud, willfully and knowingly misleads or threatens\u2014 (I) the person whose return or claim for refund is being prepared, or (II) a prospective person seeking for a return or claim for refund to be prepared, or (vi) has engaged in conduct (as identified in regulations or guidance issued by the Secretary) which is similar to the conduct described in clauses (i) through (v) and that the denial, suspension, or revocation of such number would promote compliance with the requirements of this title and effective tax administration. (B) Monetary penalty (i) In general In addition to, or in lieu of, any suspension or revocation of a preparer tax identification number under subparagraph (A), the Secretary may impose a penalty in any amount not exceeding\u2014 (I) in the case of any determination made by the Secretary with respect to a tax return preparer which is described in subparagraph (A) (with the exception of clause (v) of such subparagraph), $1,000 with respect to each such determination, and (II) in the case of any determination made by the Secretary with respect to a tax return preparer which is described in subparagraph (A)(v), $5,000 with respect to each such determination. (ii) Reduction Any penalty imposed under clause (i) shall be reduced by the amount of any penalty imposed under section 6694, 6695, 6700, 6701, or 6702 with regard to the same conduct. (iii) Adjustment for inflation (I) In general In the case of any penalty imposed during any calendar year beginning after 2025, the $1,000 amount in clause (i)(I) and the $5,000 amount in clause (i)(II) shall each be increased by an amount equal to\u2014 (aa) such dollar amount, multiplied by (bb) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year, determined by substituting calendar year 2024 for calendar year 2016 in subparagraph (A)(ii) thereof. (II) Rounding If any amount determined under subclause (I) is not a multiple of $100, such amount shall be rounded to the nearest multiple of $100. (C) Reinstatement The Secretary shall, through regulations or other guidance, establish procedures to allow any tax return preparer whose preparer tax identification number has been suspended or revoked pursuant to subparagraph (A) to have such number reissued (or, in the case of a suspension, for such suspension to be terminated), provided that such preparer demonstrates, to the satisfaction of the Secretary, that\u2014 (i) the conduct described in such paragraph which was the basis for such suspension or revocation has been sufficiently addressed or resolved (such as through completion of educational programs described in paragraph (3) or reinstatement of a license issued by a State for the preparation of tax returns), and (ii) effective tax administration would be promoted by terminating the suspension of such number or reissuing such number to such preparer. (D) Preliminary suspension (i) In general After notice and opportunity to respond, the Secretary may suspend the preparer tax identification number of a tax return preparer for a period of not greater than 180 days if the Secretary determines that\u2014 (I) such tax return preparer has engaged in any conduct described in clauses (i) through (vi) of subparagraph (A), and (II) such suspension is necessary to prevent serious economic harm to taxpayers or serious impairment of effective tax administration, such as to prevent the filing of fraudulent returns or claims for refund. (ii) Limitation For purposes of clause (i), if the preparer tax identification number of a tax return preparer has been suspended pursuant to such clause 2 times during any 5-year period, the Secretary may not issue an additional suspension pursuant to such clause with respect to such preparer during such period unless such suspension is subsequent to a determination by the Secretary to suspend or revoke the preparer tax identification number of such preparer pursuant to subparagraph (A). (E) Regulations Not later than 24 months after the date of enactment of this subsection, the Secretary shall issue such regulations or other guidance as the Secretary determines necessary to carry out the purposes of this paragraph, including\u2014 (i) guidelines that identify the particular penalty applicable to any conduct described in subparagraph (A), and (ii) the manner of notice and opportunity to respond for purposes of subparagraph (D). (6) Appeal In the case of any tax return preparer for whom the Secretary has made a determination\u2014 (A) that such preparer has not met the requirements of paragraphs (2) and (3) or of paragraph (4) and that issuance of a preparer tax identification number should be denied, (B) under paragraph (5)(A) that the preparer tax identification number for such preparer should be suspended or revoked, or (C) that a penalty should be imposed pursuant to paragraph (5)(B), such preparer shall be provided with an opportunity to appeal such determination to the Internal Revenue Service Independent Office of Appeals pursuant to procedures (as established by the Secretary through regulations or other guidance) which are similar to the procedures provided under section 330 of title 31, United States Code, or regulations prescribed thereunder. (7) Disclosure of final determinations (A) In general In the case of any final determination with respect to the extended suspension, revocation, reissuance, or termination of an extended suspension of a preparer tax identification number under this subsection, not later than 30 days following such determination, the Secretary shall publish such determination on the public website of the Internal Revenue Service, which shall include\u2014 (i) a statement of the facts and circumstances relating to such determination, and (ii) the reasons for the determination. (B) Extended suspension For purposes of subparagraph (A), the term extended suspension means a suspension issued by the Secretary pursuant to paragraph (5)(A) for a period of greater than 180 days. (8) Preparer tax identification number For purposes of this subsection, the term preparer tax identification number means an identifying number described in subsection (a)(4)(A). .\n##### (b) Information returns of tax return preparers\nSection 6060 is amended\u2014\n**(1)**\nby redesignating subsection (c) as subsection (d), and\n**(2)**\nby inserting after subsection (b) the following:\n(c) Additional information from supervisors In the case of a person required to make a return under subsection (a) who is described in section 6109(a)(4)(B)(ii)(III), such person shall include in such return\u2014 (1) the name and taxpayer identification number of any tax return preparer under their supervision and direction who, pursuant to subparagraph (B) of section 6109(a)(4), is exempted from the requirement under subparagraph (A) of such section, (2) with respect to each tax return preparer described in paragraph (1), whether such preparer is employed by such person as of the date on which such return is made, and (3) such other information as the Secretary determines appropriate. .\n##### (c) Determinations regarding practice before the Department\nSection 330 of title 31, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (e) as subsection (f); and\n**(2)**\nby inserting after subsection (d) the following:\n(e) Disclosure of final determinations In the case of any final determination under subsection (c) or (d), not later than 30 days following such determination, the Secretary shall publish such determination on a public website, which shall include\u2014 (1) a statement of the facts and circumstances relating to such determination, and (2) the reasons for the determination. .\n##### (d) Disclosure relating to misconduct by practitioners and tax return preparers\n**(1) In general**\nSection 6103(k) is amended by adding at the end the following new paragraph:\n(16) Disclosure relating to misconduct by practitioners and tax return preparers Under such procedures as the Secretary may prescribe, the Secretary may disclose returns and return information to the extent the Secretary determines it is necessary to publish determinations pursuant to section 6109(e)(7) and section 330(e) of title 31, United States Code, provided that such disclosure is redacted to remove\u2014 (A) any name, address, or other identifying information with respect to any persons other than the representative or tax return preparer who is the subject of such determination, and (B) such other information as the Secretary determines appropriate to protect the privacy of such persons. .\n**(2) Conforming amendment**\nSection 6103(p)(3)(A) is amended by striking or (9) and inserting (9), or (16) .\n##### (e) Requirement To include identifying number for paid preparer of offer-in-Compromise\n**(1) In general**\nSection 6109(a) is amended by inserting after paragraph (4) the following new paragraph:\n(5) Furnishing identifying number for offer-in-compromise Any offer-in-compromise (as described in section 7122) which has been prepared by any person for compensation shall include such identifying number as may be prescribed for securing proper identification of such person. .\n**(2) Penalty**\nSection 7122 is amended by adding at the end the following new subsection:\n(h) Failure To furnish identifying number (1) In general (A) Penalty Any person who prepares an offer-in-compromise for compensation and who fails to include an identifying number which complies with section 6109(a)(5) with respect to such offer-in-compromise shall pay a penalty of $250 for such failure. (B) Non-compliance For purposes of this paragraph, an identifying number shall be deemed to not comply with section 6109(a)(5) if such identifying number\u2014 (i) is assigned to another person, (ii) does not exist, (iii) is inactive or expired, (iv) has been withdrawn, (v) is suspended or has been revoked, or (vi) is otherwise invalid for use by the preparer. (C) Adjustment for inflation (i) In general In the case of any documents filed during any calendar year beginning after 2025, the $250 amount in subparagraph (A) shall be increased by an amount equal to\u2014 (I) such dollar amount, multiplied by (II) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year, determined by substituting calendar year 2024 for calendar year 2016 in subparagraph (A)(ii) thereof. (ii) Rounding If any amount determined under clause (i) is not a multiple of $10, such amount shall be rounded to the nearest multiple of $10. (2) Exception The penalty imposed under paragraph (1) shall not apply if it is shown that such failure is due to reasonable cause and not due to willful neglect. (3) Limitation (A) In general The maximum penalty imposed under this subsection on any person with respect to documents filed during any calendar year shall not exceed $75,000. (B) Adjustment for inflation (i) In general In the case of any penalty imposed during any calendar year beginning after 2025, the $75,000 amount in subparagraph (A) shall be increased by an amount equal to\u2014 (I) such dollar amount, multiplied by (II) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year, determined by substituting calendar year 2024 for calendar year 2016 in subparagraph (A)(ii) thereof. (ii) Rounding If any amount determined under clause (i) is not a multiple of $1,000, such amount shall be rounded to the nearest multiple of $1,000. (4) Other applicable rules Rules similar to the rules of section 6696 shall apply for purposes of this subsection. .\n##### (f) GAO Study and report on the exchange of information between the IRS and State taxation authorities\n**(1) In general**\nNot later than 18 months after the date of the enactment of this Act, the Comptroller General of the United States shall conduct a study and submit to Congress a report on the sharing of information between the Secretary and State authorities, as authorized under subsections (d) and (k)(5) of section 6103 of the Internal Revenue Code of 1986, regarding identification numbers issued to paid tax return preparers and return preparer minimum standards.\n**(2) Increased information sharing**\nThe study and report described in paragraph (1) shall include an analysis of the impact that increased information sharing between Federal and State authorities would have on efforts to enforce minimum standards on paid tax return preparers.\n##### (g) Publication of common errors and penalties\nNot later than 36 months after the date of the enactment of this Act and annually thereafter, the Commissioner of the Internal Revenue shall publish on the public website of the Internal Revenue Service\u2014\n**(1)**\nthe 10 most frequent errors found on tax returns which were prepared by tax return preparers (as defined in section 7701(a)(36) of the Internal Revenue Code of 1986) during the preceding calendar year, and\n**(2)**\nwith respect to the preceding calendar year, the top 10 reasons that tax return preparers were\u2014\n**(A)**\nsubject to penalties imposed under the Internal Revenue Code of 1986, or\n**(B)**\notherwise disciplined under section 6109 of such Code or section 330 of title 31, United States Code.\n##### (h) Rule of construction\nNothing in this section (or amendment made by this section) shall be construed to require the Secretary to eliminate or terminate any existing program or authority\u2014\n**(1)**\nwhich, pursuant to section 330 of title 31, United States Code, permits a tax return preparer to represent a taxpayer before the Department of the Treasury in cases in which such preparer prepared and signed the return of tax, or\n**(2)**\nfor publication of a public database on the website of the Internal Revenue Service of tax return preparers who have satisfied the requirements for issuance of a preparer tax identification number (as defined in section 6109(e)(8) of the Internal Revenue Code of 1986).\n##### (i) Effective date\n**(1) In general**\nThe amendments made by this section shall take effect on the date which is 180 days after the date of enactment of this Act.\n**(2) Transition rules for educational requirements for tax return preparers**\n**(A) Annual Filing Season Program**\nIn the case of any tax return preparer who, as of the date of enactment of this Act, has received a record of completion with respect to the Annual Filing Season Program established by the Internal Revenue Service, such tax return preparer shall be deemed to have satisfied the education requirements of section 6109(e)(3) of the Internal Revenue Code of 1986 (as added by this section) for the calendar year for which such record of completion applies.\n**(B) Approved courses**\nIn the case of any entity which, as of the date of enactment of this Act, is approved to provide continuing education for purposes of the Annual Filing Season Program established by the Internal Revenue Service, such entity shall be deemed to satisfy the applicable requirements under section 6109(e)(3) of the Internal Revenue Code of 1986 until the date on which the Secretary has\u2014\n**(i)**\nissued such regulations or other guidance as the Secretary determines necessary for purposes of establishing standards for educational programs under such section, and\n**(ii)**\npursuant to subparagraph (E) of such section, published a list of educational programs which have been determined by the Secretary to satisfy the applicable requirements under such section.",
      "versionDate": "2025-11-28",
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
        "actionDate": "2026-02-26",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3931",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "TAS Act",
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
        "name": "Taxation",
        "updateDate": "2025-12-16T17:05:43Z"
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
      "date": "2025-11-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6323ih.xml"
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
      "title": "Taxpayer Protection and Preparer Proficiency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-16T09:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Taxpayer Protection and Preparer Proficiency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-16T09:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to penalize improper compliance with certain taxpayer requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-16T09:18:21Z"
    }
  ]
}
```
