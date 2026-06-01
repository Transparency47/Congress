# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3663?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3663
- Title: NDO Fairness Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3663
- Origin chamber: Senate
- Introduced date: 2026-01-15
- Update date: 2026-05-20T15:43:20Z
- Update date including text: 2026-05-20T15:43:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-01-15: Introduced in Senate
- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-01-15: Introduced in Senate

## Actions

- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3663",
    "number": "3663",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "NDO Fairness Act of 2026",
    "type": "S",
    "updateDate": "2026-05-20T15:43:20Z",
    "updateDateIncludingText": "2026-05-20T15:43:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-15",
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
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T17:35:27Z",
          "name": "Referred To"
        }
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "UT"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "TN"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "TX"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "VT"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3663is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3663\nIN THE SENATE OF THE UNITED STATES\nJanuary 15, 2026 Mr. Coons (for himself and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to modify delayed notice requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the NDO Fairness Act of 2026 .\n#### 2. Preclusion of notice\n##### (a) In general\nSubsection (b) of section 2705 of title 18, United States Code, is amended to read as follows:\n(b) Preclusion of Notice (1) Application (A) In general A governmental entity that is seeking a warrant, order, or subpoena under section 2703, when it is not required to notify the customer or subscriber, or to the extent that it may delay such notice pursuant to subsection (a), may apply to a court for an order, subject to paragraph (6), directing a provider of electronic communications service or remote computing service to which a warrant, order, or subpoena under section 2703 is directed not to notify any other person of the existence of the warrant, order, or subpoena. (B) Length An order granted under subparagraph (A) shall be in effect\u2014 (i) for a period of not more than 1 year if the nature of the offense for which the governmental entity is seeking the warrant, order, or subpoena pertains to child pornography under section 2256, sexual exploitation of children under section 2251, or any Federal, State, Tribal, or military offense that is the substantial equivalent; or (ii) for a period of not more than 90 days for all other investigations. (C) Other requirements (i) In general An application for an order under subparagraph (A) shall state, to the best of the applicant\u2019s knowledge, whether the named customer or subscriber whose information is sought by the warrant, order, or subpoena under section 2703\u2014 (I) is aware of the warrant, order, subpoena, or underlying investigation; and (II) is suspected of involvement in the commission of the crime under investigation. (ii) Orders An order granted under subparagraph (A) may not direct, or otherwise require, a provider of electronic communications service or remote computing service to provide notification of the expiration of the order to the court or government entity that sought the order. (2) Determination (A) In general The court may not grant a request for an order made under paragraph (1), or an extension of such order requested by the governmental entity pursuant to paragraph (3), unless\u2014 (i) the court issues a written determination, based on specific and articulable facts, and including written findings of fact and conclusions of law, that it is likely that not granting the request will result in\u2014 (I) endangering the life or physical safety of an individual; (II) flight from prosecution; (III) destruction of or tampering with evidence; (IV) intimidation of potential witnesses; or (V) otherwise seriously jeopardizing an investigation or unduly delaying a trial; (ii) the order is narrowly tailored and there is no less restrictive alternative, including notification to an individual or organization within or providing legal representation to the named customer or subscriber, that is not likely to result in an adverse result as described in subclauses (I) through (V) of clause (i); and (iii) the court has reviewed the individual warrant, order, or subpoena under section 2703 to which the order issued under paragraph (1) applies. (B) Nature of the offense (i) In general Subject to clause (ii), the court may consider the nature of the offense in issuing a determination under subparagraph (A). (ii) Presumption If the court determines there is a reasonable belief the nature of the offense pertains to child pornography, as defined in section 2256, or sexual exploitation of children, as described in section 2251, or any Federal, State, Tribal, or military offense that is the substantial equivalent, the court may presume that 1 or more of the adverse results described in subclauses (I) through (V) of subparagraph (A)(i) are met and may issue an order consistent with this subsection without a written decision under subparagraph (A)(i). (3) Extension A governmental entity may request 1 or more extensions of an order granted under paragraph (1) of not more than 90 days for each such extension. The court may only grant such an extension if the court issues the written determination required under paragraph (2)(A). (4) Notification of changed circumstances If the need for the order issued under paragraph (1) or extended under paragraph (3) changes materially, the governmental entity that requested the order or extension shall notify the court within a reasonable period of time (not to exceed 14 days) of the changed circumstances, and the court shall reassess the order and modify or vacate as appropriate. (5) Opportunity to be heard (A) In general Upon an application, petition, or motion by a provider of electronic communications service or remote computing service or person acting on behalf of the provider to which an order under paragraph (1) has been issued, including any extension of such order under paragraph (3), the court may modify or vacate the order if\u2014 (i) the order does not meet requirements under this subsection; or (ii) compliance with the order is unreasonable or otherwise unlawful. (B) Stay of disclosure of named customer or subscriber communications or records A provider's obligation to disclose the information requested in the warrant, order, or subpoena to which the order in paragraph (1) applies is stayed upon the filing of the application, petition, or motion under this paragraph pending resolution of the application, petition, or motion, unless the court with jurisdiction over the challenge determines based on a showing by the governmental entity that the stay should be lifted in whole or in part prior to resolution. (C) Finality of order The decision of the court resolving an application, petition, or motion under this paragraph shall constitute a final, appealable order. (6) Exception A provider of electronic communications service or remote computing service to which an order under paragraph (1), including any extension of such order under paragraph (3), applies, or an officer, employee, or agent thereof, may disclose information otherwise subject to any applicable nondisclosure requirement to\u2014 (A) those persons to whom disclosure is necessary in order to comply with the warrant, order, or subpoena; (B) an attorney in order to obtain legal advice or assistance regarding the order issued under paragraph (1), including any extension of such order under paragraph (3), or the warrant, order, or subpoena to which the order applies; and (C) any person the court determines can be notified of the warrant, order, or subpoena. (7) Scope of nondisclosure Any person to whom disclosure is made under paragraph (6) (other than the governmental entity) shall be subject to the nondisclosure requirements applicable to the person to whom the order is issued. Any recipient authorized under this subsection to disclose to a person information otherwise subject to a nondisclosure requirement shall notify the person of the applicable nondisclosure requirement. (8) Supporting documentation Upon serving a provider of electronic communications service or remote computing service with an order granted under paragraph (1), including any extension of such order under paragraph (3), the governmental entity shall include a copy of the warrant, order, or subpoena to which the nondisclosure order applies. (9) Expiration of order precluding notice Upon expiration of an order issued under paragraph (1) or, if an extension has been granted under paragraph (3), expiration of the extension, the governmental entity shall deliver to the named customer or subscriber, by at least 2 methods, which shall be personal service, registered or first-class mail, electronic mail, or other means approved by the court as reasonably calculated to reach the named customer or subscriber within 5 business days of the expiration of the order\u2014 (A) a copy of the warrant, order, or subpoena; and (B) notice that informs the named customer or subscriber\u2014 (i) of the nature of the law enforcement inquiry with reasonable specificity; (ii) that information maintained for such customer or subscriber by the provider of electronic communications service or remote computing service to which the warrant, order, or subpoena under section 2703, was directed, supplied to, or requested by the government entity; (iii) that notification of such customer or subscriber was precluded by court order; (iv) of the identity of the court authorizing the preclusion of notice; (v) of the provision of this chapter under which the preclusion of notice was authorized; and (vi) that the government will, upon request by the customer or subscriber made within 180 days after receiving notification under this paragraph, provide the named customer or subscriber with a copy of the information that was disclosed in response to the warrant, order, or subpoena, or in the event that no information was disclosed, a written certification that no information was disclosed. (10) Copy of information disclosed Upon expiration of the order precluding notice issued under paragraph (1), including any extension of such order under paragraph (3), and at the request of the named customer or subscriber made within 180 days of receiving notification under paragraph (9), the governmental entity shall promptly provide the named customer or subscriber\u2014 (A) with a copy of the information that was disclosed in response to the warrant, order, or subpoena except\u2014 (i) illicit records; (ii) records or materials pertaining to child pornography, as defined in section 2256, or sexual exploitation of children, as described in section 2251, or any Federal, State, Tribal, or military offense that is the substantial equivalent; or (iii) other illegal material; or (B) in the event that no information was disclosed, a written certification that no information was disclosed. (11) Redactions Any information disclosed pursuant to paragraph (9) or (10) may be redacted only if a court finds such redactions necessary to preserve the secrecy or integrity of an investigation. .\n##### (b) Additional provisions regarding delayed notice\nSection 2705 of title 18, United States Code, is amended by adding at the end the following:\n(c) Annual report (1) In general On an annual basis, the Attorney General shall provide to the Committee on the Judiciary of the Senate , the Committee on the Judiciary of the House of Representatives , and the Director of the Administrative Office of the United States Courts, which the Attorney General shall publish on the website of the Department of Justice, in a manner consistent with protection of national security, a report setting forth with respect to the preceding calendar year, for each Federal judicial district\u2014 (A) the number of named customers or subscribers with respect to whom, in that calendar year, a warrant, subpoena, or court order was issued pursuant to section 2703; (B) the aggregate number of applications requesting delay of notification pursuant to subsection (a)(1), preclusion of notice pursuant to subsection (b)(1), and extensions pursuant to subsection (b)(3); (C) the aggregate number of orders under this section either granting, extending, or denying a request for delay of notification or preclusion of notice; (D) the aggregate number of orders under this section affecting a member of the news media, including any conduct related to activities protected under the First Amendment to the Constitution of the United States; and (E) the aggregate number of arrests, trials, and convictions, resulting from investigations in which orders under this section were obtained, including the offenses for which individuals were arrested, tried, or convicted. (2) Process The Attorney General shall include in the report under this subsection a description of the process and the information used to determine the numbers for each of subparagraphs (A) through (E) of paragraph (1). .",
      "versionDate": "2026-01-15",
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
        "actionDate": "2025-11-20",
        "text": "Ordered to be Reported (Amended) by Voice Vote."
      },
      "number": "6048",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "NDO Fairness Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-02-11T18:08:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-15",
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
          "measure-id": "id119s3663",
          "measure-number": "3663",
          "measure-type": "s",
          "orig-publish-date": "2026-01-15",
          "originChamber": "SENATE",
          "update-date": "2026-05-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3663v00",
            "update-date": "2026-05-20"
          },
          "action-date": "2026-01-15",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>NDO Fairness Act of 2026</strong><br/>\u00a0<br/>This bill increases the requirements the government must meet to obtain a nondisclosure order (NDO) under the Stored Communications Act (SCA).</p><p>The SCA generally prohibits providers of remote computing services or electronic communication services (providers) from disclosing stored electronic communications or records (e.g., emails) or information pertaining to customers or subscribers. However, the SCA authorizes the government seek a warrant, order, or subpoena to compel providers to disclose electronic communications or records or information pertaining to customers or subscribers during an investigation. Providers may notify customers and subscribers of the warrant, order, or subpoena unless the government obtains a court order\u2014an NDO\u2014that delays the notification.</p><p>This bill raises the standard the government must meet to obtain (or extend) an NDO. The bill also requires the court, before issuing an NDO, to issue a written determination that the standard was met based on specific and articulable facts, and to review the underlying warrant, order, or subpoena.</p><p>The bill requires NDOs to be narrowly tailored. It also limits their duration to 90 days for most investigations, though it permits a duration of up to one year for investigations pertaining to an offense involving child pornography or sexual exploitation of children.</p><p>Finally, the bill requires the Department of Justice to report annually on NDO-related\u00a0data, including the number of customers or subscribers targeted; applications for orders; orders granted, extended, or denied; and orders targeting members of the media or conduct related to certain protected activities.</p>"
        },
        "title": "NDO Fairness Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3663.xml",
    "summary": {
      "actionDate": "2026-01-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>NDO Fairness Act of 2026</strong><br/>\u00a0<br/>This bill increases the requirements the government must meet to obtain a nondisclosure order (NDO) under the Stored Communications Act (SCA).</p><p>The SCA generally prohibits providers of remote computing services or electronic communication services (providers) from disclosing stored electronic communications or records (e.g., emails) or information pertaining to customers or subscribers. However, the SCA authorizes the government seek a warrant, order, or subpoena to compel providers to disclose electronic communications or records or information pertaining to customers or subscribers during an investigation. Providers may notify customers and subscribers of the warrant, order, or subpoena unless the government obtains a court order\u2014an NDO\u2014that delays the notification.</p><p>This bill raises the standard the government must meet to obtain (or extend) an NDO. The bill also requires the court, before issuing an NDO, to issue a written determination that the standard was met based on specific and articulable facts, and to review the underlying warrant, order, or subpoena.</p><p>The bill requires NDOs to be narrowly tailored. It also limits their duration to 90 days for most investigations, though it permits a duration of up to one year for investigations pertaining to an offense involving child pornography or sexual exploitation of children.</p><p>Finally, the bill requires the Department of Justice to report annually on NDO-related\u00a0data, including the number of customers or subscribers targeted; applications for orders; orders granted, extended, or denied; and orders targeting members of the media or conduct related to certain protected activities.</p>",
      "updateDate": "2026-05-20",
      "versionCode": "id119s3663"
    },
    "title": "NDO Fairness Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-01-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>NDO Fairness Act of 2026</strong><br/>\u00a0<br/>This bill increases the requirements the government must meet to obtain a nondisclosure order (NDO) under the Stored Communications Act (SCA).</p><p>The SCA generally prohibits providers of remote computing services or electronic communication services (providers) from disclosing stored electronic communications or records (e.g., emails) or information pertaining to customers or subscribers. However, the SCA authorizes the government seek a warrant, order, or subpoena to compel providers to disclose electronic communications or records or information pertaining to customers or subscribers during an investigation. Providers may notify customers and subscribers of the warrant, order, or subpoena unless the government obtains a court order\u2014an NDO\u2014that delays the notification.</p><p>This bill raises the standard the government must meet to obtain (or extend) an NDO. The bill also requires the court, before issuing an NDO, to issue a written determination that the standard was met based on specific and articulable facts, and to review the underlying warrant, order, or subpoena.</p><p>The bill requires NDOs to be narrowly tailored. It also limits their duration to 90 days for most investigations, though it permits a duration of up to one year for investigations pertaining to an offense involving child pornography or sexual exploitation of children.</p><p>Finally, the bill requires the Department of Justice to report annually on NDO-related\u00a0data, including the number of customers or subscribers targeted; applications for orders; orders granted, extended, or denied; and orders targeting members of the media or conduct related to certain protected activities.</p>",
      "updateDate": "2026-05-20",
      "versionCode": "id119s3663"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3663is.xml"
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
      "title": "NDO Fairness Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-06T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "NDO Fairness Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-06T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to modify delayed notice requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-06T03:18:33Z"
    }
  ]
}
```
