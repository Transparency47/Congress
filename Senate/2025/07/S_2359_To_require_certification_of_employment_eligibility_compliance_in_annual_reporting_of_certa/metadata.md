# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2359?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2359
- Title: SAFE HIRE Act
- Congress: 119
- Bill type: S
- Bill number: 2359
- Origin chamber: Senate
- Introduced date: 2025-07-21
- Update date: 2025-09-12T14:46:43Z
- Update date including text: 2025-09-12T14:46:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-21: Introduced in Senate
- 2025-07-21 - IntroReferral: Introduced in Senate
- 2025-07-21 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-21: Introduced in Senate

## Actions

- 2025-07-21 - IntroReferral: Introduced in Senate
- 2025-07-21 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-21",
    "latestAction": {
      "actionDate": "2025-07-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2359",
    "number": "2359",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001242",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Moreno, Bernie [R-OH]",
        "lastName": "Moreno",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "SAFE HIRE Act",
    "type": "S",
    "updateDate": "2025-09-12T14:46:43Z",
    "updateDateIncludingText": "2025-09-12T14:46:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-21",
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
      "actionDate": "2025-07-21",
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
          "date": "2025-07-21T20:10:43Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2359is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2359\nIN THE SENATE OF THE UNITED STATES\nJuly 21, 2025 Mr. Moreno introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require certification of employment eligibility compliance in annual reporting of certain securities issuers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strengthening Accountability for Employers Hiring Individuals and Reforming Enforcement Act or the SAFE HIRE Act .\n#### 2. Executive certification of employment eligibility compliance\nSection 13 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78m ) is amended by adding at the end the following:\n(t) Certification Requirements (1) Definitions In this subsection: (A) Covered employer The term covered employer means any issuer of a security registered under section 12 or person required to file a report under section 15(d). (B) Internal controls The term internal controls means policies, procedures, and systems reasonably designed to\u2014 (i) ensure compliance with employment eligibility verification requirements under Federal law, including section 274A of the Immigration and Nationality Act ( 8 U.S.C. 1324a ); (ii) identify and prevent the use of fraudulent or unauthorized documentation in the hiring process; and (iii) promptly detect, report, and remediate any known violations of such requirements. (C) Principal executive officer The term principal executive officer has the meaning given in section 229.402(a)(3) of title 17, Code of Federal Regulations, or any successor regulation. (D) Principal human resources officer The term principal human resources officer means the most senior officer of a covered employer with responsibility for human capital management, including employment eligibility policies and compliance. (2) Certification The principal executive officer and the principal human resources officer (or officers performing similar functions) of each covered employer shall submit with each annual report filed under subsection (a) or section 15(d) the following: (A) A certification that\u2014 (i) the certifying officers have reviewed the report; (ii) based on the knowledge of the certifying officers, the report does not contain any untrue statement of a material fact or omit to state a material fact necessary to make the statements made, in light of the circumstances, not misleading; (iii) based on the knowledge of the certifying officers, the report fairly presents, in all material respects, the employment practices of the issuer, including the number and legal work status of persons employed; (iv) the certifying officers\u2014 (I) are responsible for establishing and maintaining internal controls with respect to employment eligibility verification (including Form I\u20139 compliance and E-Verify); (II) have designed such internal controls to ensure that material information relating to compliance with section 274A of the Immigration and Nationality Act ( 8 U.S.C. 1324a ) is made known to such officers by others within the company; (III) have evaluated the effectiveness of the internal controls described in subclause (II) not less than 90 days prior to the submission of the report; and (IV) have presented in the report their conclusions about the effectiveness of such internal controls based on their evaluation; and (v) the certifying officers have disclosed to the Department of Homeland Security and the Department of Justice\u2014 (I) all significant deficiencies in the internal controls of the covered employer which could adversely affect the ability of the covered employer to ensure compliance with Federal employment eligibility requirements; and (II) any known material violation of section 274A of the Immigration and Nationality Act ( 8 U.S.C. 1324a ), including the employment of unauthorized aliens, as defined in subsection (h) of that section. (B) A list of all disclosed significant deficiencies and known material violations described in subparagraph (A)(v). (3) Criminal penalties for false certification (A) In general It shall be unlawful for a principal executive officer or principal human resources officer (or other officer performing similar functions) of a covered employer to\u2014 (i) certify any statement described in paragraph (2)(A) knowing that the report does not comply with the requirements therein; or (ii) willfully fail to make the certification under paragraph (2)(A) or submit the list of disclosed significant deficiencies and known material violations pursuant to paragraph (2)(B). (B) Penalties (i) In general Any individual who violates subparagraph (A) shall be fined not more than $1,000,000, imprisoned not more than 10 years, or both. (ii) Enhanced penalty Any individual who violates subparagraph (A) with respect to the employment of unauthorized aliens in violation of section 274A(a)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1324a(a)(1) ) shall be fined not more than $5,000,000, imprisoned not more than 20 years, or both. .\n#### 3. Implementation and rulemaking\nNot later than 1 year after the date of enactment of this Act, the Chair of the Securities and Exchange Commission, in consultation with the Secretary of Homeland Security and the Attorney General, shall\u2014\n**(1)**\nprescribe rules requiring the inclusion of the certification described in section 13(t) of the Securities and Exchange Act of 1934, as added by section 2, within the annual reports filed on Form 10\u2013K or any successor form;\n**(2)**\nestablish requirements for public availability of such certifications; and\n**(3)**\npromulgate any regulations necessary to carry out the purposes of this Act and the amendments made by this Act.",
      "versionDate": "2025-07-21",
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
        "updateDate": "2025-09-12T14:46:43Z"
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
      "date": "2025-07-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2359is.xml"
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
      "title": "SAFE HIRE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAFE HIRE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strengthening Accountability for Employers Hiring Individuals and Reforming Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require certification of employment eligibility compliance in annual reporting of certain securities issuers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-02T03:18:27Z"
    }
  ]
}
```
