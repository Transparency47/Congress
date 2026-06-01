# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2322?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2322
- Title: Appraisal Modernization Act
- Congress: 119
- Bill type: S
- Bill number: 2322
- Origin chamber: Senate
- Introduced date: 2025-07-17
- Update date: 2025-12-17T12:03:16Z
- Update date including text: 2025-12-17T12:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in Senate
- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-17: Introduced in Senate

## Actions

- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2322",
    "number": "2322",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "W000790",
        "district": "",
        "firstName": "Raphael",
        "fullName": "Sen. Warnock, Raphael G. [D-GA]",
        "lastName": "Warnock",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Appraisal Modernization Act",
    "type": "S",
    "updateDate": "2025-12-17T12:03:16Z",
    "updateDateIncludingText": "2025-12-17T12:03:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T16:22:51Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "MD"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "DE"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NJ"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NJ"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "MA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "VA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2322is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2322\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Mr. Warnock (for himself, Ms. Alsobrooks , Ms. Blunt Rochester , Mr. Kim , Mr. Booker , and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Federal Housing Enterprises Safety and Soundness Act of 1992 to require that financial institutions, appraisal management companies, appraisers, and other valuation professionals are serving the housing market in a manner that is efficient and consistent for all mortgage loan applicants, borrowers, and communities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Appraisal Modernization Act .\n#### 2. Public appraisal database\n##### (a) In general\nThe Federal Housing Enterprises Safety and Soundness Act of 1992 ( 12 U.S.C. 4501 et seq. ) is amended by inserting after section 1313B ( 12 U.S.C. 4513b ) the following:\n1313C. Public appraisal database (a) Purpose The purpose of this section is to provide the public, the Federal Government, and State governments with residential real estate appraisal data to help determine whether financial institutions, appraisal management companies, appraisers, and other valuation professionals are serving the housing market in a manner that is efficient and consistent for all mortgage loan applicants, borrowers, and communities. (b) Definitions In this section: (1) Application The term application means the submission of a consumer\u2019s financial information for the purposes of obtaining an extension of credit. (2) Dwelling The term dwelling \u2014 (A) means a 1-to-4 unit residential structure, whether or not attached to real property; and (B) includes a detached home, an individual condominium or cooperative unit, and a manufactured home or other factory-built home. (3) Financial institution The term financial institution means any partnership, company, corporation, association (incorporated or unincorporated), trust, estate, cooperative organization, or other entity that engages in financial activity. (4) Mortgage loan The term mortgage loan means any extension of credit that is secured by a lien on a dwelling. (c) Agency Appraisal Data Sharing (1) Legacy appraisal data Not later than 180 days after the date of enactment of this section, the Federal National Mortgage Association, the Federal Home Loan Mortgage Corporation, the Federal Housing Administration, the Department of Agriculture, and the Department of Veterans Affairs shall provide to the Agency\u2014 (A) the appraisal data collected in connection with mortgage loan applications and mortgage loans that financial institutions submitted to the Federal National Mortgage Association, the Federal Home Loan Mortgage Corporation, the Federal Housing Administration, the Department of Agriculture, and the Department of Veterans Affairs, as applicable, during the period beginning on January 1, 2017, and ending on the date of enactment of this section; and (B) the corresponding census tract of the subject property, agency loan identifier, the Universal Loan Identifier required by the Home Mortgage Disclosure Act of 1975 ( 12 U.S.C. 2801 et seq. ), the mortgage loan purpose, whether the property is owner occupied, the acquiring agency, and the race and ethnicity of the borrower as required by that Act. (2) Modernized appraisal data Not later than 1 year after the date of enactment of this section, and on a quarterly basis thereafter, the Federal National Mortgage Association, the Federal Home Loan Mortgage Corporation, the Federal Housing Administration, the Department of Agriculture, and the Department of Veterans Affairs shall provide to the Agency\u2014 (A) the appraisal data collected in connection with mortgage loan applications and mortgage loans that financial institutions submitted in the previous quarter to the Federal National Mortgage Association, the Federal Home Loan Mortgage Corporation, the Federal Housing Administration, the Department of Agriculture, and the Department of Veterans Affairs, as applicable; and (B) the corresponding census tract of the subject property, agency loan identifier, the Universal Loan Identifier required by the Home Mortgage Disclosure Act of 1975 ( 12 U.S.C. 2801 et seq. ), the mortgage loan purpose, whether the property is owner occupied, the acquiring agency, and the race and ethnicity of the borrower as required by that Act. (d) Public searchable database (1) Legacy appraisal database Not later than 2 years after the date of enactment of this section, the Director, in consultation with the Secretary of Housing and Urban Development, the Secretary of Agriculture, and the Secretary of Veterans Affairs, shall make publicly available online a searchable and downloadable appraisal-level public use file of the data shared pursuant to subsection (c)(1). (2) Modernized appraisal database Not later than 2 years after the date of enactment of this section, and on a quarterly basis thereafter, the Director, in consultation with the Secretary of Housing and Urban Development, the Secretary of Agriculture, and the Secretary of Veterans Affairs, shall make publicly available online a searchable and downloadable appraisal-level public use file of the data shared pursuant to subsection (c)(2). (e) Form and manner of valuation data (1) In general Any appraisal data required to be disclosed under subsection (d) shall be itemized at the appraisal level to clearly and conspicuously disclose\u2014 (A) the assignment data, including the assignment reason, property valuation method, client or lender name, appraisal management company name, appraiser company name, appraiser credential level, appraiser identification number, and State, exterior scope of inspection, interior scope of inspection, and the inspection date; (B) the subject property data, including the physical address, zip code, county, State, neighborhood name, attachment type, number of units excluding accessory dwelling units, number of accessory dwelling units, special tax assessments, whether the subject property is a planned unit development, condominium, cooperative, property on Native American lands, subject site owned in common, homeowner responsible for all exterior maintenance of dwelling, or new construction, the property rights appraised, whether all rights are included in the appraisal, and the legal description; (C) the market data, including the market area boundary, search criteria description, number of active listings and their median days on market, lowest list price, median list price, and highest list price, the number of pending sales, the number of sales in the past 24 months and their lowest sale price, median sale price, and highest sale price, whether there is distressed market competition, the price trend source, the demand and supply trend, the marketing time, and the market commentary; (D) the project information, including the project information data source, the monthly amount of mandatory fees, the common amenities and services included, the utilities included, whether the developer or sponsor is in control, any known legal actions, unit special assessments, and unit tax abatements or exemptions; (E) the subject listing information, including the subject listing identification number, the start date, end date, days on market, starting list price, and current or final list price; (F) the sales contract data, including whether there is a sales contract, whether the contract was analyzed, and whether the transaction appears to be an arms length transaction, the contract price, the contract data, transfer terms, any personal property conveyed, any known sales concessions, total sales concessions and whether such concessions are typical for the market, and sales contract analysis; (G) for the subject property and each comparable property relied on for the opinion of value, as applicable\u2014 (i) the general data, including the property address, data source, proximity to the subject, list price, listing status, contract price or sale price, sales concessions, contract date, sale data, days on market, whether attached or detached, and property rights appraised; (ii) the site data, including the site size, neighborhood name, topography, site influence or location, site view, and site range; (iii) the dwelling data, including the year built, dwelling style, heating, and cooling; (iv) the energy efficient and green features, including the efficiency rating; (v) the unit data, including the number of bedrooms, number of full baths, number of half baths, finished area above grade, finished area below grade, unfinished area below grade, and below grade exterior access; (vi) the exterior quality and condition ratings data, including the quality rating, exterior walls and trim, roof, and condition rating; (vii) the interior quality and condition ratings data, including the quality rating, condition rating, kitchen, and overall flooring; (viii) the overall quality and condition ratings data, including the quality rating and the condition rating; (ix) the property amenities data, including the outdoor living, water features, and miscellaneous; (x) the vehicle storage data, including type, spaces, and detail; and (xi) for each comparable relied on for the opinion of value, any adjustments related to each of the above data fields; (H) the summary data for the comparable properties relied on for the opinion of value, including the list price, sale price, net adjustment total, price per finished area above grade, adjusted price, and comparable weight; (I) the reconciliation data, including the approaches to value, the contract price, opinion of market value, market value condition, reasonable exposure time, effective date of appraisal, and final value condition statement; (J) the corresponding census tract of the subject property, agency loan identifier, the Universal Loan Identifier required by the Home Mortgage Disclosure Act of 1975 ( 12 U.S.C. 2801 et seq. ), the mortgage loan purpose, whether the property is owner occupied, the acquiring agency, and the race and ethnicity of the borrower as required by that Act, based on the data provided by the Federal National Mortgage Association, the Federal Home Loan Mortgage Corporation, the Federal Housing Administration, the Department of Agriculture, and the Department of Veterans Affairs, as applicable, to the Agency and added to the public appraisal database by the Agency; and (K) such other information as the Agency may require by regulation, after notice and comment. (2) Discretion to modify publicly available data The Agency may modify data collected under this section, to be made publicly available, if the Agency determines by regulation, after notice and comment, that the release of the unmodified data creates risks to a mortgage loan applicant or mortgage loan borrower privacy interests that are not justified by the benefits of such release to the public in light of the statutory purposes. (f) Access to the unmodified database For enforcement and other purposes, the Agency shall, upon request, provide access to all information collected for the database pursuant to this section, in unredacted form, to any Executive agency, as defined in section 105 of title 5, United States Code, the Board of Governors of the Federal Reserve System, the Office of the Comptroller of the Currency, the Federal Deposit Insurance Corporation, the National Credit Union Administration, the Appraisal Subcommittee of the Federal Financial Institutions Examination Council, the Bureau of Consumer Financial Protection, and any State attorney general, State appraiser regulator, or other State agency with responsibility for laws related to appraisals. (g) Rule of construction Nothing in this section shall be construed to encourage unsafe or unsound lending, appraisal, or valuation practices. (h) Rules and interpretive guidelines Not later than 1 year after the date of enactment of this section, the Agency shall issue a final rule after notice and comment and issue such guidance as may be necessary to carry out and enforce this section. .\n#### 3. Reconsideration of value\n##### (a) In general\nSection 129E of the Truth In Lending Act ( 15 U.S.C. 1639e ) is amended\u2014\n**(1)**\nby redesignating subsections (j) and (k) as subsections (k) and (l), respectively; and\n**(2)**\nby inserting after subsection (i) the following:\n(j) Consumer right to reconsideration of value or subsequent appraisal (1) Definitions In this section: (A) Unacceptable appraisal practice The term unacceptable appraisal practice means an appraisal report that\u2014 (i) uses unsupported or subjective terms to assess or rate the property without providing a foundation for analysis and contextual information; (ii) uses inaccurate or incomplete data about the subject property, the neighborhood, the market area, or any comparable property; (iii) includes references, statements or comparisons about crime rates or crime statistics, whether objective or subjective; (iv) relies in the appraisal analysis on comparable properties that were not personally inspected by the appraiser when required by the appraisal\u2019s scope of work; (v) relies in the appraisal analysis on inappropriate comparable properties; (vi) fails to use comparable properties that are more similar, or nearer, to the subject property without adequate explanation; (vii) uses comparable property data provided by any interested party to the transaction without verification by a disinterested party; (viii) uses inappropriate adjustments for differences between the subject property and the comparable properties that do not reflect the market\u2019s reaction to such differences; or (ix) fails to make proper adjustments, including time adjustments for differences between the subject property and the comparable properties when necessary. (B) Unsupported The term unsupported means, with respect to an appraisal report or an appraiser\u2019s opinion of value, that the appraisal report or the opinion of value is not supported by relevant evidence and logic. (2) Review In connection with a consumer credit transaction secured by a consumer\u2019s principal dwelling, a creditor shall have a review and resolution procedure for a consumer-initiated reconsideration of value or subsequent appraisal that complies with the following requirements: (A) The creditor shall complete its own appraisal review before delivering the appraisal to the consumer. (B) The creditor shall have policies and procedures that provide the consumer with a process to submit one request for a reconsideration of value and subsequent appraisal prior to the loan closing or within 60 calendar days of denial of a credit application if the consumer believes the appraisal report may be unsupported, may be deficient due to an unacceptable appraisal practice, or may reflect discrimination. (C) At the time of application and upon delivery of the appraisal report to the consumer, the creditor shall provide a written disclosure to the consumer describing the process for requesting a reconsideration of value or subsequent appraisal, which written disclosure shall include a standardized format for the consumer to submit the request for a reconsideration of value, including\u2014 (i) the name of the borrower; (ii) the property address; (iii) the effective date of the appraisal; (iv) the appraiser\u2019s name; (v) the date of the request; (vi) a description of why the consumer believes the appraisal report may be unsupported, may be deficient due to an unacceptable appraisal practice, or may reflect discrimination; (vii) any additional information, data, including not more than 5 alternative comparable properties and the related data sources that the consumer would like the appraiser to consider; and (viii) an explanation of why the new information, data, or comparable properties support the reconsideration of value. (D) The creditor shall obtain the necessary information from the consumer if the consumer\u2019s request for reconsideration of value or subsequent appraisal is unclear or requires more information. (E) The creditor shall have a standardized format to communicate the reconsideration of value to the appraiser, which format shall include\u2014 (i) the name of the borrower; (ii) the property address; (iii) the effective date of the appraisal; (iv) the appraiser\u2019s name; (v) the date of the request; (vi) a description of any area of the appraisal report that may be unsupported, may be deficient due to an unacceptable appraisal practice, or may reflect discrimination; (vii) any additional information, data, including not more than 5 alternative comparable properties and the related data sources that the consumer would like the appraiser to consider; (viii) an explanation of why the new information, data, or comparable properties support the reconsideration of value; (ix) a definition of turn-time expectations for the appraiser to communicate the reconsideration of value results back to the creditor; (x) instructions for delivering the reconsideration of value response as part of a revised appraisal report that includes commentary on conclusions regardless of the outcome; and (xi) a reference for appraisers on how to correct minor appraisal issues or non-material errors not related to the reconsideration of value process. (3) Subsequent appraisal and referral (A) In general If the creditor identifies material deficiencies in the appraisal report that are not corrected or addressed by the appraiser upon request of the creditor, including through a consumer-initiated reconsideration of value, or if there is evidence of unsupported or unacceptable appraisal practices, the creditor shall\u2014 (i) at the request of the consumer, order a subsequent appraisal at the creditor's own expense; and (ii) forward the appraisal report and the creditor\u2019s summary of findings to the appropriate appraisal licensing agency or regulatory board. (B) Discrimination If the creditor has reason to believe that an appraisal report reflects discrimination, the creditor shall\u2014 (i) order a subsequent appraisal, at the creditor's own expense; (ii) forward the appraisal report and the creditor\u2019s summary of findings to the appropriate local, State, or Federal enforcement agency; and (iii) upon a final determination of discrimination by the appropriate local, State, or Federal enforcement agency, receive a reimbursement from the appraiser covering the cost of the subsequent appraisal ordered by the creditor. (C) Definition (i) In general Except as provided in clause (ii), in this paragraph, the term reason to believe means that the creditor has reviewed the applicable law and available evidence and determined that a potential violation of Federal or state antidiscrimination law exists. The available evidence may include the appraisal report, loan files, written communications, credible observations by persons with direct knowledge, statistical analysis, and the appraiser\u2019s response to the request for a reconsideration of value. (ii) Exception The term reason to believe does not mean that there is a final legal determination of discrimination. (4) Document retention The creditor shall retain all documentation and written communications related to the request for reconsideration of value or subsequent appraisal in the loan file during the seven-year period beginning on the date on which the consumer submitted the credit application. (5) Rule of construction This subsection is consistent with the exceptions to the appraiser independence requirements found in Section 129E(c) of the Truth in Lending Act ( 15 U.S.C. 1639e(c) ). Nothing in this subsection shall be construed to require a creditor to submit a reconsideration of value to the original appraiser before ordering a subsequent appraisal from a subsequent appraiser. .\n##### (b) Rules and interpretative guidelines\nSection 129E(g) of the Truth in Lending Act ( 15 U.S.C. 1639e(g) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking paragraph (2), the Board and inserting paragraphs (2) and (3), the Bureau ; and\n**(2)**\nby adding at the end the following:\n(3) Final rule Not later than 1 year after the date of enactment of this paragraph, the Federal Housing Finance Agency shall issue a final rule after notice and comment and issue such guidance as may be necessary to carry out and enforce subsection (j). .",
      "versionDate": "2025-07-17",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-09-05T16:16:10Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2322is.xml"
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
      "title": "Appraisal Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Appraisal Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Housing Enterprises Safety and Soundness Act of 1992 to require that financial institutions, appraisal management companies, appraisers, and other valuation professionals are serving the housing market in a manner that is efficient and consistent for all mortgage loan applicants, borrowers, and communities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T03:48:17Z"
    }
  ]
}
```
