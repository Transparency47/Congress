# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/293?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/293
- Title: WALL Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 293
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2025-05-23T20:32:39Z
- Update date including text: 2025-05-23T20:32:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/293",
    "number": "293",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001319",
        "district": "",
        "firstName": "Katie",
        "fullName": "Sen. Britt, Katie Boyd [R-AL]",
        "lastName": "Britt",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "WALL Act of 2025",
    "type": "S",
    "updateDate": "2025-05-23T20:32:39Z",
    "updateDateIncludingText": "2025-05-23T20:32:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-29",
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
      "actionDate": "2025-01-29",
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
          "date": "2025-01-29T17:35:25Z",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "TX"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "ID"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "WY"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "SD"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s293is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 293\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mrs. Britt (for herself, Mr. Cruz , Mr. Risch , Mr. Barrasso , Mr. Rounds , and Mr. Wicker ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo appropriate $25,000,000,000 for the construction of a border wall between the United States and Mexico, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the WALL Act of 2025 .\n#### 2. Mandatory spending for border wall\n##### (a) In general\nThere is appropriated $25,000,000,000 for the purpose of constructing a physical barrier along the southern land border of the United States.\n##### (b) Availability\nAmounts appropriated under subsection (a) shall remain available until expended for the purpose described in subsection (a).\n#### 3. Offsets\n##### (a) Eligibility for child tax credit\n**(1) In general**\nSection 24(e) of the Internal Revenue Code of 1986 is amended to read as follows:\n(e) Identification requirements (1) In general No credit shall be allowed under this section to a taxpayer with respect to any qualifying child unless the taxpayer includes on the return of tax for the taxable year\u2014 (A) the name of such qualifying child, and (B) the valid identification number of the taxpayer (and, in the case of a joint return, the taxpayer\u2019s spouse) and such qualifying child. (2) Valid identification number (A) In general For purposes of this subsection, the term valid identification number means\u2014 (i) in the case of the taxpayer and any spouse of the taxpayer, a social security number issued to the individual by the Social Security Administration on or before the due date for filing the return for the taxable year, and (ii) in the case of a qualifying child, a social security number issued to such child by the Social Security Administration on or before the due date for filing such return. (B) Exception for individuals prohibited from engaging in employment in United States For purposes of subparagraph (A)(i) and subsection (h)(4)(C), the term social security number shall not include the social security number of an individual who is prohibited from engaging in employment in the United States. .\n**(2) Conforming amendments**\nSubsection (h) of section 24 of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nin paragraph (1), by striking (7) and inserting (6) ,\n**(B)**\nin paragraph (4), by amending subparagraph (C) to read as follows:\n(C) Social security number required Subparagraph (A) shall not apply with respect to any dependent of the taxpayer unless the taxpayer includes on the return of tax for the taxable year, for both the taxpayer and the dependent, a social security number issued to each such individual by the Social Security Administration on or before the due date for filing such return. , and\n**(C)**\nby striking paragraph (7).\n**(3) Effective date**\nThe amendments made by this subsection shall apply to taxable years ending after the date of the enactment of this Act.\n##### (b) Individuals prohibited from engaging in employment in United States not eligible for earned income tax credit\n**(1) In general**\nSubsection (m) of section 32 of the Internal Revenue Code of 1986 is amended to read as follows:\n(m) Identification numbers (1) In general Solely for purposes of subsections (c)(1)(E) and (c)(3)(D), a taxpayer identification number means a social security number issued to an individual by the Social Security Administration on or before the due date for filing the return for the taxable year. (2) Exception for individuals prohibited from engaging in employment in United States For purposes of paragraph (1), in the case of subsection (c)(1)(E), the term social security number shall not include the social security number of an individual who is prohibited from engaging in employment in the United States. .\n**(2) Effective date**\nThe amendment made by this subsection shall apply to taxable years ending after the date of the enactment of this Act.\n##### (c) Identification requirement for American Opportunity and Lifetime Learning credits\n**(1) In general**\nSection 25A(g)(1) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(C) Social Security number required (i) In general For purposes of this paragraph, the term taxpayer identification number means a social security number issued to an individual by the Social Security Administration. (ii) Exception for individuals prohibited from engaging in employment in United States For purposes of clause (i), the term social security number shall not include the social security number of an individual who is prohibited from engaging in employment in the United States. .\n**(2) Effective date**\nThe amendment made by this subsection shall apply to all taxable years ending after the date of the enactment of this Act.\n##### (d) Fees for filing a tax return using an ITIN\n**(1) In general**\nSection 6109(i) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(5) Fee for filing tax return using an ITIN (A) In general In the case of any individual income tax return filed by a taxpayer residing in the United States, the Secretary shall require the taxpayer to pay a fee for each such return filed in an amount equal to the product of\u2014 (i) the total number of individuals included on such return (including any spouse or dependent of the taxpayer) with respect to whom an individual taxpayer identification number has been issued, multiplied by (ii) $300. (B) Exception Subparagraph (A) shall not apply to any individual who has reported to the Secretary that their social security number has been subject to theft, misuse, or misappropriation by another person. .\n**(2) Effective date**\nThe amendment made by this subsection shall apply to returns the due date for which (determined without regard to extensions) is after the date of the enactment of this Act.\n##### (e) Ensuring validity of Social Security numbers\n**(1) In general**\nSection 6109 of the Internal Revenue Code of 1986 is amended by inserting after subsection (d) the following new subsection:\n(e) Confirmation of social security numbers For purposes of paragraphs (1) and (3) of subsection (a), the Secretary, in coordination with the Commissioner of Social Security, shall verify that any social security account number submitted by a person, or with respect to another person, in any return, statement, or other document is\u2014 (1) the correct social security account number as issued to such person by the Commissioner of Social Security, and (2) valid and otherwise unexpired as of the date of submission of such return, statement, or other document. .\n**(2) Effective date**\nThe amendment made by this subsection shall apply to returns, statements, and other documents submitted after the date of the enactment of this Act.\n##### (f) Requiring agencies To use E-Verify To Confirm satisfactory immigration status for eligibility for certain federally funded benefits\n**(1) In general**\nSection 1137(a) of the Social Security Act ( 42 U.S.C. 1320b\u20137(a) ) is amended\u2014\n**(A)**\nin paragraph (6), by striking ; and and inserting a semicolon;\n**(B)**\nin paragraph (7), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(8) with respect to any applicant for, or recipient of, benefits under a program listed in subsection (b) who is a noncitizen and whose eligibility for such benefits is conditional upon such applicant or recipient having an immigration status that allows the applicant or recipient to work in the United States, the State agency administering such program shall use the employment eligibility confirmation program described in section 403(a) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1324a note) (also known as E\u2013Verify ) to confirm that such applicant or recipient has such status, and shall deny eligibility for such benefits to any such applicant or recipient who does not have such status. .\n**(2) Federal housing programs**\n**(A)**\nSection 8(o)(6) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o)(6) ) is amended by adding at the end the following:\n(D) Verification of immigration status For each dwelling unit for which a housing assistance payment contract is established under this subsection, the public housing agency shall, with respect to any prospective tenant of the dwelling unit who is a noncitizen and whose eligibility for assistance is conditional upon the tenant having an immigration status that allows the tenant to work in the United States, use the employment eligibility confirmation program described in section 403(a) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1324a note) (commonly known as E\u2013Verify ) to confirm that the tenant has such status and shall deny eligibility for such assistance to any tenant who does not have such status. .\n**(B)**\nSection 8(o)(13) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o)(13) ) is amended by adding at the end the following:\n(P) Verification of immigration status For each dwelling unit in a project for which a housing assistance payment contract is established under this subsection, the public housing agency shall, with respect to any prospective tenant of the dwelling unit who is a noncitizen and whose eligibility for assistance is conditional upon the tenant having an immigration status that allows the tenant to work in the United States, use the employment eligibility confirmation program described in section 403(a) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1324a note) (commonly known as E\u2013Verify ) to confirm that the tenant has such status and shall deny eligibility for such assistance to any tenant who does not have such status. .\n**(C)**\nSection 3(a) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(a) ) is amended by adding at the end the following:\n(10) Verification of immigration status For each public housing dwelling unit owned, assisted, or operated by a public housing agency, the public housing agency shall, with respect to any prospective tenant of the dwelling unit who is a noncitizen and whose eligibility for assistance is conditional upon the tenant having an immigration status that allows the tenant to work in the United States, use the employment eligibility confirmation program described in section 403(a) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1324a note) (commonly known as E\u2013Verify ) to confirm that the tenant has such status and shall deny eligibility for such assistance to any tenant who does not have such status. .\n**(D)**\nSection 202(i) of the Housing Act of 1959 ( 12 U.S.C. 1701q(i) ) is amended by adding at the end the following:\n(3) Verification of immigration status For each dwelling unit assisted under this section, the owner shall, with respect to any prospective tenant of the dwelling unit who is a noncitizen and whose eligibility for assistance is conditional upon the tenant having an immigration status that allows the tenant to work in the United States, use the employment eligibility confirmation program described in section 403(a) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1324a note) (commonly known as E\u2013Verify ) to confirm that the tenant has such status and shall deny eligibility for such assistance to any tenant who does not have such status. .\n**(E)**\nSection 811(i)(1) of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 8013(i)(1) ) is amended by adding at the end the following:\n(E) Verification of immigration status For each dwelling unit assisted under this section, the owner shall, with respect to any prospective tenant of the dwelling unit who is a noncitizen and whose eligibility for assistance is conditional upon the tenant having an immigration status that allows the tenant to work in the United States, use the employment eligibility confirmation program described in section 403(a) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1324a note) (commonly known as E\u2013Verify ) to confirm that the tenant has such status and shall deny eligibility for such assistance to any tenant who does not have such status. .\n**(3) Rulemaking**\n**(A) In general**\nThe Secretary of Agriculture, the Secretary of Health and Human Services, and the Secretary of Labor shall promulgate rules to implement section 1137(a)(8) of the Social Security Act, as added by paragraph (1), which requires the use of E\u2013Verify to verify applicant eligibility for certain programs administered by their respective departments.\n**(B) Housing programs**\nThe Secretary of Housing and Urban Development shall promulgate rules to implement amendments made by subparagraphs (A) through (E) of paragraph (2), which require the use of E\u2013Verify to verify tenant eligibility for housing assistance programs administered by the Department of Housing and Urban Development.\n**(4) Effective date**\nThe amendments made by this subsection shall take effect on the date of enactment of this Act.\n#### 4. Minimum fines for illegal entry and overstay\n##### (a) Illegal entry\nChapter 8 of title II of the Immigration and Nationality Act ( 8 U.S.C. 1321 et seq. ) is amended\u2014\n**(1)**\nin section 275 ( 8 U.S.C. 1325 )\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nby striking (1) ;\n**(ii)**\nby striking or (2) ;\n**(iii)**\nby striking (3) ; and\n**(iv)**\nby striking shall, for and all that follows and inserting the following: \u201cshall\u2014\n(1) for the first commission of any such offense, be fined in accordance with subsection (b), imprisoned not more than 6 months, or both; and (2) for a subsequent commission of any such offense, be fined in accordance with subsection (b), imprisoned not more than 2 years, or both. ; and\n**(B)**\nin subsection (b)\u2014\n**(i)**\nby inserting (1) before Any alien ;\n**(ii)**\nby striking civil penalty of and all that follows through the period at the end of paragraph (2) and inserting civil penalty in an amount equal to not less than $3,000 and not more than $10,000. ; and\n**(iii)**\nin the undesignated matter at the end, by striking Civil penalties and inserting the following:\n(2) Civil penalties ; and\n**(2)**\nin section 276 ( 8 U.S.C. 1326 ), by amending subsection (a) to read as follows:\n(a) (1) Subject to paragraph (2) and subsection (b), any alien who, after being denied admission, excluded, deported, or removed or after departing the United States while an order of exclusion, deportation, or removal is outstanding, enters, attempts to enter, or is at any time found in, the United States, shall be subject to a civil penalty in an amount equal to not less than $3,000 and not more than $10,000. (2) Notwithstanding paragraph (1), an alien described in such paragraph shall not be subject to the civil penalty described in such paragraph if\u2014 (A) before reembarking at a place outside the United States or applying for admission from a foreign contiguous territory, the Secretary of Homeland Security has expressly consented to such alien's reapplying for admission; or (B) with respect to an alien previously denied admission and removed, such alien establishes that he or she was not required to obtain such advance consent under this Act. .\n##### (b) Overstay\nSection 222(g) of the Immigration and Nationality Act ( 8 U.S.C. 1202(g) ) is amended by adding at the end the following:\n(3) An alien described in paragraph (1) shall be subject to a civil penalty in an amount equal to the product of $50 multiplied by the number of months the alien remained in the United States beyond the alien\u2019s authorized period of stay. .",
      "versionDate": "2025-01-29",
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
        "updateDate": "2025-03-06T13:09:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-29",
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
          "measure-id": "id119s293",
          "measure-number": "293",
          "measure-type": "s",
          "orig-publish-date": "2025-01-29",
          "originChamber": "SENATE",
          "update-date": "2025-05-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s293v00",
            "update-date": "2025-05-23"
          },
          "action-date": "2025-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>WALL Act of 2025 </strong></p><p>This bill appropriates $25 billion for the construction of a wall on the U.S.-Mexico border and addresses other issues related to immigration.</p><p>As offsets to this spending, the bill restricts the child tax credit, earned income credits, and lifetime learning credits to those with Social Security numbers who are not prohibited from employment in the United States. Also, individuals who file taxes using an individual taxpayer identification number (ITIN) instead of a Social Security number must pay a fee ($300 for each individual on the tax return using an ITIN).</p><p>The bill restricts eligibility for certain federally\u00a0funded benefits, including unemployment compensation, supplemental nutrition assistance, and housing benefits, to those eligible to work in the United States. Agencies administering such benefits must use the E-Verify program to confirm the eligibility of applicants for such benefits.</p><p>This bill also sets fines for non-U.S. nationals (<em>aliens</em> under federal law) who improperly enter the United States or overstay their visas.</p>"
        },
        "title": "WALL Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s293.xml",
    "summary": {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>WALL Act of 2025 </strong></p><p>This bill appropriates $25 billion for the construction of a wall on the U.S.-Mexico border and addresses other issues related to immigration.</p><p>As offsets to this spending, the bill restricts the child tax credit, earned income credits, and lifetime learning credits to those with Social Security numbers who are not prohibited from employment in the United States. Also, individuals who file taxes using an individual taxpayer identification number (ITIN) instead of a Social Security number must pay a fee ($300 for each individual on the tax return using an ITIN).</p><p>The bill restricts eligibility for certain federally\u00a0funded benefits, including unemployment compensation, supplemental nutrition assistance, and housing benefits, to those eligible to work in the United States. Agencies administering such benefits must use the E-Verify program to confirm the eligibility of applicants for such benefits.</p><p>This bill also sets fines for non-U.S. nationals (<em>aliens</em> under federal law) who improperly enter the United States or overstay their visas.</p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119s293"
    },
    "title": "WALL Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>WALL Act of 2025 </strong></p><p>This bill appropriates $25 billion for the construction of a wall on the U.S.-Mexico border and addresses other issues related to immigration.</p><p>As offsets to this spending, the bill restricts the child tax credit, earned income credits, and lifetime learning credits to those with Social Security numbers who are not prohibited from employment in the United States. Also, individuals who file taxes using an individual taxpayer identification number (ITIN) instead of a Social Security number must pay a fee ($300 for each individual on the tax return using an ITIN).</p><p>The bill restricts eligibility for certain federally\u00a0funded benefits, including unemployment compensation, supplemental nutrition assistance, and housing benefits, to those eligible to work in the United States. Agencies administering such benefits must use the E-Verify program to confirm the eligibility of applicants for such benefits.</p><p>This bill also sets fines for non-U.S. nationals (<em>aliens</em> under federal law) who improperly enter the United States or overstay their visas.</p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119s293"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s293is.xml"
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
      "title": "WALL Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-04T12:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "WALL Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to appropriate $25,000,000,000 for the construction of a border wall between the United States and Mexico, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:19Z"
    }
  ]
}
```
