# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/163?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/163
- Title: Protecting Students on Campus Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 163
- Origin chamber: Senate
- Introduced date: 2025-01-21
- Update date: 2026-01-07T16:57:53Z
- Update date including text: 2026-01-07T16:57:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in Senate
- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-04-30 - Committee: Committee on Health, Education, Labor, and Pensions. Committee consideration and Mark Up Session held.
- Latest action: 2025-01-21: Introduced in Senate

## Actions

- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-04-30 - Committee: Committee on Health, Education, Labor, and Pensions. Committee consideration and Mark Up Session held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/163",
    "number": "163",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Protecting Students on Campus Act of 2025",
    "type": "S",
    "updateDate": "2026-01-07T16:57:53Z",
    "updateDateIncludingText": "2026-01-07T16:57:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Committee consideration and Mark Up Session held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-21",
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
      "actionDate": "2025-01-21",
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
            "date": "2025-04-30T21:39:03Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-21T20:30:46Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "PA"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "ME"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NV"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "NV"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s163is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 163\nIN THE SENATE OF THE UNITED STATES\nJanuary 21, 2025 Mr. Cassidy (for himself and Mr. Fetterman ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo require institutions of higher education participating in Federal student aid programs to share information about title VI of the Civil Rights Act of 1964, including a link to the webpage of the Office for Civil Rights where an individual can submit a complaint regarding discrimination in violation of such title, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Students on Campus Act of 2025 .\n#### 2. Title VI awareness campaign\n##### (a) Title VI awareness campaign\n**(1) In general**\nThe Secretary of Education, acting through the Assistant Secretary for Civil Rights of the Department of Education, shall carry out a public awareness campaign regarding the availability of rights provided to individuals under title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ).\n**(2) Awareness campaign**\nThe public awareness campaign shall include appealing visual and auditory elements and shall be updated annually and distributed to institutions of higher education for physical posting in 1 or more high traffic public places, such as student centers, and digital posting on 1 or more high traffic institution web pages, such as student services. The campaign shall utilize such methods and materials as necessary to maximize student accessibility.\n**(3) Ability to contract**\nThe Secretary may carry out this subsection directly or through a contract with a nonprofit organization that specializes in public awareness communications.\n##### (b) HEA Amendments\nSection 487(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1094(a) ) is amended by adding at the end the following:\n(30) The institution\u2014 (A) has prominently displayed on the homepage of the institution a link to the webpage of the Office for Civil Rights of the Department of Education where an individual can submit a complaint regarding discrimination on the basis of race, color, or national origin in violation of title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ); and (B) will annually display and post the public awareness campaign materials created and distributed under section 2(a) of the Protecting Students on Campus Act of 2025 in high traffic public places on campus, such as student centers, and high traffic institution web pages, such as student services. .\n#### 3. Congressional briefings\n##### (a) In General\nBeginning not later than 30 days after the date of enactment of this Act and ending 1 year after the date of enactment of this Act, the Assistant Secretary for Civil Rights of the Department of Education shall give a monthly briefing to Congress\u2014\n**(1)**\nexplaining the number of complaints that the Office for Civil Rights of the Department of Education (referred to in this Act as the Office ) has received in the previous month regarding discrimination on the basis of race, color, or national origin in violation of title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ), disaggregated by the basis of discrimination;\n**(2)**\ndescribing how the Office plans to address those complaints and the investigations opened in response to those complaints; and\n**(3)**\nproviding data about the length of time that those complaints remain open after being received by the Office.\n##### (b) Report\nNot later than 48 hours prior to each briefing described in subsection (a), the Assistant Secretary for Civil Rights of the Department of Education shall provide a written report to Congress that contains the information that will be presented at the next briefing, in a manner that protects personally identifiable information in accordance with applicable privacy laws.\n#### 4. Audit and study\n##### (a) Requirement To submit data\nEach institution of higher education receiving Federal funds shall submit an annual report to the Inspector General of the Department of Education that includes\u2014\n**(1)**\nthe number of complaints regarding discrimination on the basis of race, color, or national origin in violation of title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ) that were submitted to the institution in the previous year;\n**(2)**\nan analysis of the number of such complaints and their substance; and\n**(3)**\na narrative of the action the institution took with respect to such complaints.\n##### (b) Audit\nThe Inspector General of the Department of Education shall complete an annual audit of the institutions of higher education that are in the top 5 percent of institutions based on the per capita number of complaints described in subsection (a) received by the institutions, controlling for student population, to examine the process for addressing such complaints and the need for any referrals to the Office for Civil Rights of the Department of Education.\n##### (c) Study\nThe Inspector General of the Department of Education shall conduct a study\u2014\n**(1)**\nregarding why there is a disparity between the complaints regarding discrimination on the basis of race, color, or national origin in violation of title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ) that are submitted to institutions of higher education and such complaints that are submitted to the Office; and\n**(2)**\nquantifying the distinction described in paragraph (1).\n#### 5. OCR process reforms\nThe Office for Civil Rights of the Department of Education shall not close or dismiss any complaint due to resolution by another Federal, State, or local civil rights enforcement agency or through a recipient\u2019s internal grievance procedures.",
      "versionDate": "2025-01-21",
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
        "actionDate": "2025-12-18",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "6857",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting Students on Campus Act of 2025",
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
            "name": "Congressional oversight",
            "updateDate": "2025-03-19T15:06:21Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-03-19T15:05:55Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-19T15:06:09Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-03-19T15:06:30Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-03-19T15:05:49Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-03-19T15:06:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-02-24T20:25:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-21",
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
          "measure-id": "id119s163",
          "measure-number": "163",
          "measure-type": "s",
          "orig-publish-date": "2025-01-21",
          "originChamber": "SENATE",
          "update-date": "2025-04-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s163v00",
            "update-date": "2025-04-04"
          },
          "action-date": "2025-01-21",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting Students on Campus Act of 2025</strong></p><p>This bill requires the Department of Education (ED) and institutions of higher education (IHEs) participating in federal student aid programs to distribute information on how to report alleged violations of civil rights under Title VI of the Civil Rights Act of 1964. (Title VI of the Civil Rights Act of 1964 prohibits discrimination based on race, color, or national origin in federally funded programs or activities.)</p><p>Specifically, the bill requires ED's Office for Civil Rights (OCR) to conduct a public awareness campaign regarding the rights\u00a0of individuals under Title VI. This campaign must be updated annually and distributed to IHEs.</p><p>The bill requires an IHE to post a link on its website on how to file a Title VI complaint with OCR. Additionally, the\u00a0IHE must annually post the materials from OCR's public awareness campaign. The information must be posted in high-traffic public places on campus (e.g., student centers) and high-traffic websites (e.g., the website for student services).\u00a0</p><p>OCR must give monthly congressional briefings on (1) the number of complaints filed with OCR, (2) how OCR plans to address those complaints and the investigations opened in response to those complaints, and (3) how long those complaints remain open.\u00a0Additionally, the bill prohibits OCR from closing or dismissing a complaint due to resolution via another agency or avenue.\u00a0</p><p>The bill also requires annual reporting by IHEs on discrimination complaints. Further, the bill directs ED's Office of Inspector General to audit and study discrimination complaints.</p>"
        },
        "title": "Protecting Students on Campus Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s163.xml",
    "summary": {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Students on Campus Act of 2025</strong></p><p>This bill requires the Department of Education (ED) and institutions of higher education (IHEs) participating in federal student aid programs to distribute information on how to report alleged violations of civil rights under Title VI of the Civil Rights Act of 1964. (Title VI of the Civil Rights Act of 1964 prohibits discrimination based on race, color, or national origin in federally funded programs or activities.)</p><p>Specifically, the bill requires ED's Office for Civil Rights (OCR) to conduct a public awareness campaign regarding the rights\u00a0of individuals under Title VI. This campaign must be updated annually and distributed to IHEs.</p><p>The bill requires an IHE to post a link on its website on how to file a Title VI complaint with OCR. Additionally, the\u00a0IHE must annually post the materials from OCR's public awareness campaign. The information must be posted in high-traffic public places on campus (e.g., student centers) and high-traffic websites (e.g., the website for student services).\u00a0</p><p>OCR must give monthly congressional briefings on (1) the number of complaints filed with OCR, (2) how OCR plans to address those complaints and the investigations opened in response to those complaints, and (3) how long those complaints remain open.\u00a0Additionally, the bill prohibits OCR from closing or dismissing a complaint due to resolution via another agency or avenue.\u00a0</p><p>The bill also requires annual reporting by IHEs on discrimination complaints. Further, the bill directs ED's Office of Inspector General to audit and study discrimination complaints.</p>",
      "updateDate": "2025-04-04",
      "versionCode": "id119s163"
    },
    "title": "Protecting Students on Campus Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Students on Campus Act of 2025</strong></p><p>This bill requires the Department of Education (ED) and institutions of higher education (IHEs) participating in federal student aid programs to distribute information on how to report alleged violations of civil rights under Title VI of the Civil Rights Act of 1964. (Title VI of the Civil Rights Act of 1964 prohibits discrimination based on race, color, or national origin in federally funded programs or activities.)</p><p>Specifically, the bill requires ED's Office for Civil Rights (OCR) to conduct a public awareness campaign regarding the rights\u00a0of individuals under Title VI. This campaign must be updated annually and distributed to IHEs.</p><p>The bill requires an IHE to post a link on its website on how to file a Title VI complaint with OCR. Additionally, the\u00a0IHE must annually post the materials from OCR's public awareness campaign. The information must be posted in high-traffic public places on campus (e.g., student centers) and high-traffic websites (e.g., the website for student services).\u00a0</p><p>OCR must give monthly congressional briefings on (1) the number of complaints filed with OCR, (2) how OCR plans to address those complaints and the investigations opened in response to those complaints, and (3) how long those complaints remain open.\u00a0Additionally, the bill prohibits OCR from closing or dismissing a complaint due to resolution via another agency or avenue.\u00a0</p><p>The bill also requires annual reporting by IHEs on discrimination complaints. Further, the bill directs ED's Office of Inspector General to audit and study discrimination complaints.</p>",
      "updateDate": "2025-04-04",
      "versionCode": "id119s163"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s163is.xml"
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
      "title": "Protecting Students on Campus Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-16T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Students on Campus Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require institutions of higher education participating in Federal student aid programs to share information about title VI of the Civil Rights Act of 1964, including a link to the webpage of the Office for Civil Rights where an individual can submit a complaint regarding discrimination in violation of such title, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:18:16Z"
    }
  ]
}
```
