# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1912?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1912
- Title: Protecting Veteran Community Care Act
- Congress: 119
- Bill type: S
- Bill number: 1912
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-02-04T01:53:44Z
- Update date including text: 2026-02-04T01:53:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1912",
    "number": "1912",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000618",
        "district": "",
        "firstName": "Steve",
        "fullName": "Sen. Daines, Steve [R-MT]",
        "lastName": "Daines",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Protecting Veteran Community Care Act",
    "type": "S",
    "updateDate": "2026-02-04T01:53:44Z",
    "updateDateIncludingText": "2026-02-04T01:53:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-22",
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
          "date": "2025-05-22T19:57:41Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "WY"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "IA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1912is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1912\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Daines (for himself, Ms. Lummis , and Mr. Grassley ) introduced the following bill; which was read twice and referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to expand access to the Veterans Community Care Program of the Department of Veterans Affairs to include certain veterans seeking mental health or substance-use services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Veteran Community Care Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nOn June 6, 2018, the John S. McCain III, Daniel K. Akaka, and Samuel R. Johnson VA Maintaining Internal Systems and Strengthening Integrated Outside Networks Act of 2018 ( Public Law 115\u2013182 ) (in this section referred to as the VA MISSION Act ) became law.\n**(2)**\nCongressional intent with the VA MISSION Act was to reform and replace the program under section 101 of the Veterans Access, Choice, and Accountability Act of 2014 ( Public Law 113\u2013146 ; 38 U.S.C. 1701 note) to ensure access of veterans to community health care providers.\n**(3)**\nThe eligibility standards established by the VA MISSION Act were not meant to be used to limit health care options for veterans or to be applied to community providers, which would result in reduced health care options.\n**(4)**\nMany veterans do not have access to a medical facility of the Department of Veterans Affairs in their community and each medical facility of the Department may not be able to adequately address the specific health care needs of a particular veteran.\n**(5)**\nIt was intent of Congress in the VA MISSION Act that all medical services, including mental health treatments and institutional extended care services for mental health, were to be available to veterans in the community.\n**(6)**\nThe Department is limiting access of veterans to community care for mental health treatments.\n**(7)**\nDespite the best efforts of the Department, veteran suicide remains at significant levels throughout the United States.\n**(8)**\nNo veteran should have to wait 30 days for mental health services to be approved by the Department.\n**(9)**\nTelehealth appointments represent a valuable complementary health care option for underserved veterans, but do not offer the same quality of care as in-person visits to facilities of the Department or in the community for veterans in crisis.\n#### 3. Expansion of Veterans Community Care Program to include access to mental health or substance-use services for veterans unable to timely access Mental Health Residential Treatment Programs\n##### (a) In general\nSection 1703 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (1)\n**(i)**\nin subparagraph (D), by striking ; or and inserting a semicolon;\n**(ii)**\nin subparagraph (E), by striking the period at the end and inserting ; or ; and\n**(iii)**\nby adding at the end the following new subparagraph:\n(F) in the case of residential mental health or substance-use services, the covered veteran\u2014 (i) meets the criteria of the Department for priority admission to a Mental Health Residential Rehabilitation Treatment Program of the Department and the Department is unable to accommodate such priority admission; or (ii) has contacted the Department to request such services from a Mental Health Residential Rehabilitation Treatment Program of the Department and the Department is not able to furnish such services in a manner than complies with the access standards of the Department for specialty care provided under this section by a health care provider specified in subsection (c). ; and\n**(B)**\nby adding at the end the following new paragraph (5):\n(5) In the case of a covered veteran entitled to mental health or substance-use services under paragraph (1)(F), the Secretary shall ensure that referral of a veteran to an alternate Mental Health Residential Rehabilitation Treatment Program of the Department does not take precedence over timely access to such services under this section pursuant to such paragraph unless such referral is requested by the covered veteran. ;\n**(2)**\nby redesignating subsection (q) as subsection (r); and\n**(3)**\nby inserting after subsection (p) the following new subsection (q):\n(q) Minimum standards for residential mental health or substance-Use services (1) Subject to paragraph (2), in furnishing residential mental health or substance-use services to covered veterans pursuant to subsection (d)(1)(F), the Secretary shall ensure that programs or facilities providing such services under this section meet the following standards: (A) A treatment program or facility must be licensed and accredited by a State for the provision of the services provided. (B) A treatment program must be accredited under either the Joint Commission Behavioral Health Standards or the Behavioral Health Standards manual (residential treatment) of the Commission on Accreditation of Rehabilitation Facilities, or any successor standards or manual. (2) If a program or facility to which a covered veteran is to be referred pursuant to subsection (d)(1)(F) does not meet the standards specified under paragraph (1), the Secretary, acting through the director of the facility of the Department carrying out the referral\u2014 (A) shall consider an alternate program or facility; and (B) may waive such standards on an individual basis if no other alternate program or facility is available or such waiver is in the best interest of the veteran. .\n##### (b) Modification of access standards\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall develop or amend existing access standards of the Department of Veterans Affairs to ensure that access to mental health care under the Veterans Community Care Program under section 1703 of title 38, United States Code, as amended by subsection (a), is not more restrictive than the access standards for specialty care under such section.\n#### 4. Prohibition on certain limitations on access of veterans to care\nSection 1703(n) of title 38, United States Code, is amended by adding at the end the following new paragraphs:\n(3) In applying wait times or access standards under this section for purposes of determining eligibility of a covered veteran for care or services under this section, the Secretary may not determine that the veteran is ineligible for such care or services due solely to the fact that health care providers specified in subsection (c) are unable to provide such care or services in compliance with such wait times or access standards. (4) If multiple options are available to a covered veteran for care or services under this section, the Secretary shall permit the veteran to elect the option that the veteran prefers. .\n#### 5. Development of community care metrics\n##### (a) In general\nSection 1703(m)(1) of title 38, United States Code, is amended by adding at the end the following new subparagraph:\n(C) The review submitted under subparagraph (A) shall include, for the year covered by the review, the following: (i) The number of instances of care or services requested. (ii) The number of such requests that were approved. (iii) The number of such requests that were denied. (iv) The number of appeals under subsection (f) of such requests that were denied, including the final decision of such appeal. (v) The eligibility criteria under which each eligible veteran has qualified for care or services under this section. (vi) Data with respect to the following: (I) Requests for care or services relating to mental health. (II) Authorizations for emergency care, including whether transportation for such care was required or whether further care or a hospital stay was required. .\n##### (b) Application\nThe amendment made by subsection (a) shall apply to each review conducted under subparagraph (A) of such section after the date of the enactment of this Act.\n#### 6. Limitation on modification of community care access standards\nAny modification on or after the date of the enactment of this Act by the Secretary of Veterans Affairs of the conditions under which care is required to be provided under section 1703(d) of title 38, United States Code, either through a modification of the designated access standards under paragraph (1)(D) of such section, a modification of the criteria developed by the Secretary under paragraph (1)(E) of such section, or otherwise through regulation, shall not take effect until a joint resolution is enacted approving such modification to the conditions under which care is required to be provided under such section.",
      "versionDate": "2025-05-22",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-23T18:37:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-22",
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
          "measure-id": "id119s1912",
          "measure-number": "1912",
          "measure-type": "s",
          "orig-publish-date": "2025-05-22",
          "originChamber": "SENATE",
          "update-date": "2026-02-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1912v00",
            "update-date": "2026-02-04"
          },
          "action-date": "2025-05-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Protecting Veteran Community Care Act</b></p> <p>This bill requires the Department of Veterans Affairs (VA) to furnish residential mental health or substance-use services to certain veterans through the Veterans Community Care Program (VCCP). Specifically, the VA must furnish such care if a veteran (1) meets VA criteria for priority admission to a VA Mental Health Residential Rehabilitation Treatment Program and the VA is unable to accommodate priority admission, or (2) has contacted the VA to request such mental health services and the VA is not able to furnish such services in a manner that complies with VA access standards for specialty care provided under the VCCP. </p> <p>The VA must ensure that a referral to an alternate Mental Health Residential Rehabilitation Treatment Program does not take precedence over timely access to mental health or substance-use services unless the referral is requested by the veteran.</p> <p>The VA is prohibited from determining a veteran is ineligible for VCCP care solely because VCCP providers are unable to comply with wait times or access standards.</p> <p>If multiple options for care or services are available, the VA must permit a veteran to elect the option the veteran prefers.</p> <p>Additionally, the bill provides minimum standards for residential mental health or substance-use services provided under the VCCP (e.g., treatment programs or facilities must be licensed and accredited for the specified services).</p>"
        },
        "title": "Protecting Veteran Community Care Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1912.xml",
    "summary": {
      "actionDate": "2025-05-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Protecting Veteran Community Care Act</b></p> <p>This bill requires the Department of Veterans Affairs (VA) to furnish residential mental health or substance-use services to certain veterans through the Veterans Community Care Program (VCCP). Specifically, the VA must furnish such care if a veteran (1) meets VA criteria for priority admission to a VA Mental Health Residential Rehabilitation Treatment Program and the VA is unable to accommodate priority admission, or (2) has contacted the VA to request such mental health services and the VA is not able to furnish such services in a manner that complies with VA access standards for specialty care provided under the VCCP. </p> <p>The VA must ensure that a referral to an alternate Mental Health Residential Rehabilitation Treatment Program does not take precedence over timely access to mental health or substance-use services unless the referral is requested by the veteran.</p> <p>The VA is prohibited from determining a veteran is ineligible for VCCP care solely because VCCP providers are unable to comply with wait times or access standards.</p> <p>If multiple options for care or services are available, the VA must permit a veteran to elect the option the veteran prefers.</p> <p>Additionally, the bill provides minimum standards for residential mental health or substance-use services provided under the VCCP (e.g., treatment programs or facilities must be licensed and accredited for the specified services).</p>",
      "updateDate": "2026-02-04",
      "versionCode": "id119s1912"
    },
    "title": "Protecting Veteran Community Care Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Protecting Veteran Community Care Act</b></p> <p>This bill requires the Department of Veterans Affairs (VA) to furnish residential mental health or substance-use services to certain veterans through the Veterans Community Care Program (VCCP). Specifically, the VA must furnish such care if a veteran (1) meets VA criteria for priority admission to a VA Mental Health Residential Rehabilitation Treatment Program and the VA is unable to accommodate priority admission, or (2) has contacted the VA to request such mental health services and the VA is not able to furnish such services in a manner that complies with VA access standards for specialty care provided under the VCCP. </p> <p>The VA must ensure that a referral to an alternate Mental Health Residential Rehabilitation Treatment Program does not take precedence over timely access to mental health or substance-use services unless the referral is requested by the veteran.</p> <p>The VA is prohibited from determining a veteran is ineligible for VCCP care solely because VCCP providers are unable to comply with wait times or access standards.</p> <p>If multiple options for care or services are available, the VA must permit a veteran to elect the option the veteran prefers.</p> <p>Additionally, the bill provides minimum standards for residential mental health or substance-use services provided under the VCCP (e.g., treatment programs or facilities must be licensed and accredited for the specified services).</p>",
      "updateDate": "2026-02-04",
      "versionCode": "id119s1912"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1912is.xml"
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
      "title": "Protecting Veteran Community Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Veteran Community Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to expand access to the Veterans Community Care Program of the Department of Veterans Affairs to include certain veterans seeking mental health or substance-use services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:24Z"
    }
  ]
}
```
