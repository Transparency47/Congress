# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8737?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8737
- Title: Never Fight Alone Act
- Congress: 119
- Bill type: HR
- Bill number: 8737
- Origin chamber: House
- Introduced date: 2026-05-12
- Update date: 2026-05-30T09:23:27Z
- Update date including text: 2026-05-30T09:23:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-12: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- Latest action: 2026-05-12: Introduced in House

## Actions

- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8737",
    "number": "8737",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "P000622",
        "district": "1",
        "firstName": "Jimmy",
        "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
        "lastName": "Patronis",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Never Fight Alone Act",
    "type": "HR",
    "updateDate": "2026-05-30T09:23:27Z",
    "updateDateIncludingText": "2026-05-30T09:23:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-12",
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
      "actionDate": "2026-05-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-12",
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
          "date": "2026-05-12T16:03:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
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
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "FL"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "FL"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NC"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "AZ"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "FL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NY"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "WI"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "KS"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "IN"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "FL"
    },
    {
      "bioguideId": "F000485",
      "district": "14",
      "firstName": "Clay",
      "fullName": "Rep. Fuller, Clay [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Fuller",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "GA"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8737ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8737\nIN THE HOUSE OF REPRESENTATIVES\nMay 12, 2026 Mr. Patronis (for himself, Mrs. Luna , Mr. Webster of Florida , Mr. Davis of North Carolina , Mr. Ciscomani , Mr. Bilirakis , Mr. Lawler , and Mr. Grothman ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to expand access to the Veterans Community Care Program of the Department of Veterans Affairs to include certain veterans seeking mental health or substance-use services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Never Fight Alone Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nOn June 6, 2018, the John S. McCain III, Daniel K. Akaka, and Samuel R. Johnson VA Maintaining Internal Systems and Strengthening Integrated Outside Networks Act of 2018 ( Public Law 115\u2013182 ) (in this section referred to as the VA MISSION Act ) became law.\n**(2)**\nCongressional intent with the VA MISSION Act was to reform and replace the program under section 101 of the Veterans Access, Choice, and Accountability Act of 2014 ( Public Law 113\u2013146 ; 38 U.S.C. 1701 note) to ensure access of veterans to community health care providers.\n**(3)**\nThe eligibility standards established by the VA MISSION Act were not meant to be used to limit health care options for veterans or to be applied to community providers, which would result in reduced health care options.\n**(4)**\nMany veterans do not have access to a medical facility of the Department of Veterans Affairs in their community and each medical facility of the Department may not be able to adequately address the specific health care needs of a particular veteran.\n**(5)**\nIt was the intent of Congress in the VA MISSION Act that all medical services, including mental health treatments and institutional extended care services for mental health, were to be available to veterans in the community.\n**(6)**\nThe Department is limiting access of veterans to community care for mental health treatments.\n**(7)**\nDespite the best efforts of the Department, veteran suicide remains at significant levels throughout the United States.\n**(8)**\nNo veteran should have to wait 30 days for mental health services to be approved by the Department.\n**(9)**\nTelehealth appointments represent a valuable complementary health care option for underserved veterans, but do not offer the same quality of care as in-person visits to facilities of the Department or in the community for veterans in crisis.\n#### 3. Expansion of Veterans Community Care Program to include access to mental health or substance-use services for veterans unable to timely access Mental Health Residential Treatment Programs\n##### (a) In general\nSection 1703 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (D), by striking ; or and inserting a semicolon;\n**(ii)**\nin subparagraph (E), by striking the period at the end and inserting ; or ; and\n**(iii)**\nby adding at the end the following new subparagraph:\n(F) in the case of residential mental health or substance-use services, the covered veteran\u2014 (i) meets the criteria of the Department for priority admission to a Mental Health Residential Rehabilitation Treatment Program of the Department and the Department is unable to accommodate such priority admission; or (ii) has contacted the Department to request such services from a Mental Health Residential Rehabilitation Treatment Program of the Department and the Department is not able to furnish such services in a manner than complies with the access standards of the Department for specialty care provided under this section by a health care provider specified in subsection (c). ; and\n**(B)**\nby adding at the end the following new paragraph (5):\n(5) In the case of a covered veteran entitled to mental health or substance-use services under paragraph (1)(F), the Secretary shall ensure that referral of a veteran to an alternate Mental Health Residential Rehabilitation Treatment Program of the Department does not take precedence over timely access to such services under this section pursuant to such paragraph unless such referral is requested by the covered veteran. ;\n**(2)**\nby redesignating subsection (q) as subsection (r); and\n**(3)**\nby inserting after subsection (p) the following new subsection (q):\n(q) Minimum standards for residential mental health or substance-Use services (1) Subject to paragraph (2), in furnishing residential mental health or substance-use services to covered veterans pursuant to subsection (d)(1)(F), the Secretary shall ensure that programs or facilities providing such services under this section meet the following standards: (A) A treatment program or facility must be licensed and accredited by a State for the provision of the services provided. (B) A treatment program must be accredited under either the Joint Commission Behavioral Health Standards or the Behavioral Health Standards manual (residential treatment) of the Commission on Accreditation of Rehabilitation Facilities, or any successor standards or manual. (2) If a program or facility to which a covered veteran is to be referred pursuant to subsection (d)(1)(F) does not meet the standards specified under paragraph (1), the Secretary, acting through the director of the facility of the Department carrying out the referral\u2014 (A) shall consider an alternate program or facility; and (B) may waive such standards on an individual basis if no other alternate program or facility is available or such waiver is in the best interest of the veteran. .\n##### (b) Modification of access standards\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall develop or amend existing access standards of the Department of Veterans Affairs to ensure that access to mental health care under the Veterans Community Care Program under section 1703 of title 38, United States Code, as amended by subsection (a), is not more restrictive than the access standards for specialty care under such section.\n#### 4. Prohibition on certain limitations on access of veterans to care\nSection 1703(n) of title 38, United States Code, is amended by adding at the end the following new paragraphs:\n(3) In applying wait times or access standards under this section for purposes of determining eligibility of a covered veteran for care or services under this section, the Secretary may not determine that the veteran is ineligible for such care or services due solely to the fact that health care providers specified in subsection (c) are unable to provide such care or services in compliance with such wait times or access standards. (4) If multiple options are available to a covered veteran for care or services under this section, the Secretary shall permit the veteran to elect the option that the veteran prefers. .\n#### 5. Development of community care metrics\n##### (a) In general\nSection 1703(m)(1) of title 38, United States Code, is amended by adding at the end the following new subparagraph:\n(C) The review submitted under subparagraph (A) shall include, for the year covered by the review, the following: (i) The number of instances of care or services requested. (ii) The number of such requests that were approved. (iii) The number of such requests that were denied. (iv) The number of appeals under subsection (f) of such requests that were denied, including the final decision of such appeal. (v) The eligibility criteria under which each eligible veteran has qualified for care or services under this section. (vi) Data with respect to the following: (I) Requests for care or services relating to mental health. (II) Authorizations for emergency care, including whether transportation for such care was required or whether further care or a hospital stay was required. .\n##### (b) Application\nThe amendment made by subsection (a) shall apply to each review conducted under subparagraph (A) of such section after the date of the enactment of this Act.\n#### 6. Limitation on modification of community care access standards\nExcept as provided in section 3(b), any modification on or after the date of the enactment of this Act by the Secretary of Veterans Affairs of the conditions under which care is required to be provided under section 1703(d) of title 38, United States Code, either through a modification of the designated access standards under paragraph (1)(D) of such section, a modification of the criteria developed by the Secretary under paragraph (1)(E) of such section, or otherwise through regulation, shall not take effect until a joint resolution is enacted approving such modification to the conditions under which care is required to be provided under such section.",
      "versionDate": "2026-05-12",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8737ih.xml"
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
      "title": "Never Fight Alone Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T09:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Never Fight Alone Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-30T09:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to expand access to the Veterans Community Care Program of the Department of Veterans Affairs to include certain veterans seeking mental health or substance-use services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T09:18:27Z"
    }
  ]
}
```
