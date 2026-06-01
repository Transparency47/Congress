# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4098?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4098
- Title: Artificial Intelligence-Ready Data Act
- Congress: 119
- Bill type: S
- Bill number: 4098
- Origin chamber: Senate
- Introduced date: 2026-03-16
- Update date: 2026-03-31T20:34:49Z
- Update date including text: 2026-03-31T20:34:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-16: Introduced in Senate
- 2026-03-16 - IntroReferral: Introduced in Senate
- 2026-03-16 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-03-16: Introduced in Senate

## Actions

- 2026-03-16 - IntroReferral: Introduced in Senate
- 2026-03-16 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-16",
    "latestAction": {
      "actionDate": "2026-03-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4098",
    "number": "4098",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Artificial Intelligence-Ready Data Act",
    "type": "S",
    "updateDate": "2026-03-31T20:34:49Z",
    "updateDateIncludingText": "2026-03-31T20:34:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-16",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-16",
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
          "date": "2026-03-16T19:59:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4098is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4098\nIN THE SENATE OF THE UNITED STATES\nMarch 16, 2026 Mr. Budd (for himself and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo establish standards and guidelines to make open Government data assets artificial intelligence-ready, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Artificial Intelligence-Ready Data Act .\n#### 2. Establishment of standards and guidelines to make open Government data assets artificial intelligence-ready\nThe National Institute of Standards and Technology Act ( 15 U.S.C. 271 et seq. ) is amended by adding at the end the following:\n37. Standards and guidelines to make open Government data assets artificial intelligence-ready (a) In general The Director shall, in consultation with the Secretary of Commerce, the Director of the Office of Science and Technology Policy, the Director of the Office of Management and Budget, and the head of any other Federal agency the Director considers appropriate, develop standards and guidelines to assist Federal agencies with making open Government data assets (as defined in section 3502 of title 44, United States Code) artificial intelligence-ready. (b) Requirements (1) Adaptability and interoperability In developing the standards and guidelines under subsection (a), the Director shall set baseline standards and guidelines for all Federal agencies that, to the greatest extent practicable, allow for the heads of the agencies to adapt and extend such standards and guidelines to meet the needs of agency-specific missions. (2) Elements The standards and guidelines required by subsection (a) shall\u2014 (A) recommend improvements to the availability and utility of open Government data assets for the development of artificial intelligence (as defined in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 )) by private or public sector entities, including\u2014 (i) for the training of artificial intelligence models or systems; (ii) best practices for data quality, data stewardship, metadata, and documentation; and (iii) ways to manage intellectual property concerns when Federal data is combined with proprietary data; (B) identify, or recommend methods for identifying, other data assets (as defined in section 3502 of title 44, United States Code) generated or maintained by Federal agencies that should be made available for the development of artificial intelligence; and (C) recommend measurements for evaluating the effectiveness of Federal agency action pertaining to subparagraphs (A) and (B). (3) Artificial Intelligence-Ready Requirements for open government data assets The standards and guidelines developed under subsection (a) shall require open Government data assets to be, to the greatest extent practicable\u2014 (A) artificial intelligence-ready, defined based on the needs of artificial intelligence developers and information provided by persons engaged with artificial intelligence that is received through the notice and comment procedure outlined in subsection (c); (B) available for download\u2014 (i) on a publicly accessible website or other convenient method; (ii) by web-scraping; or (iii) by any other method the Director considers practicable and beneficial; (C) accurate as of the date of the publication of the open Government data asset; (D) human-readable; (E) in an open and machine-readable format, accompanied by publicly available software tools that can decode or process the data; and (F) secure and protective of individual privacy. (c) Public notice and opportunity for comment (1) In general In developing the standards and guidelines under subsection (a), and in considering revisions to the standards and guidelines under subsection (d), the Director shall\u2014 (A) publish in the Federal Register\u2014 (i) proposed standards and guidelines; and (ii) a request for feedback, including on the recommendations described in subsection (b)(2); (B) provide the public with an opportunity to comment for a period of not less than 60 days; (C) ensure public comments are available for public inspection; and (D) demonstrate consideration of the public comments received under this paragraph in the development of the standards and guidelines under subsection (a) or the revision of the standards and guidelines under subsection (d). (2) Timeline for publication The Director shall publish\u2014 (A) the standards and guidelines developed under subsection (a) in the Federal Register not later than 1 year after the date of the enactment of this section; and (B) any revision to the standards and guidelines under subsection (d), or a notice that public comment had been considered and proposed revisions are not beneficial or necessary, in the Federal Register not later than 60 days after the Director has completed the review required by that subsection. (d) Updates to the standards and guidelines Not later than 2 years after the date on which the Director submits the standards and guidelines to the Director of the Office of Science and Technology Policy under subsection (e) and not less frequently than once every 2 years thereafter, the Director shall consider, in accordance with the notice and comment procedures under subsection (c), revisions to the standards and guidelines required by subsection (a) to improve the utility of the standards and guidelines. (e) Submission to the Director of the Office of Science and Technology Policy The Director shall submit the standards and guidelines developed under subsection (a), and any revision of the standards and guidelines under subsection (d), to the President for issuing requirements in accordance with section 701 of the National Science and Technology Policy, Organization, and Priorities Act of 1976. .\n#### 3. Implementation of standards and guidelines to make open Government data assets artificial intelligence-ready\nThe National Science and Technology Policy, Organization, and Priorities Act of 1976 ( 42 U.S.C. 6611 et seq. ) is amended by adding at the end the following:\nVII Implementation of standards and guidelines to make open government data assets artificial intelligence-ready 701. Implementation of standards and guidelines by Federal agencies (a) In general Upon receiving the standards and guidelines from the Director of the National Institute of Standards and Technology pursuant to section 37(e) of the National Institute of Standards and Technology Act, the President, acting through the Director of the Office of Science and Technology Policy, in consultation with the Director of the Office of Management and Budget, shall issue a requirement that the head of each Federal agency adopt such standards and guidelines. (b) Agency requirement Upon the President, acting through the Director of the Office of Science and Technology Policy, issuing a requirement to the head of a Federal agency under subsection (a), the head of such agency shall\u2014 (1) adopt and adhere to the standards and guidelines issued by the Director of the Office of Science and Technology Policy; (2) ensure that any agency-specific adaptations of the standards and guidelines remain interoperable with the data systems of other Federal agencies to support interagency collaboration; and (3) ensure that major information technology and high-performance computing acquisitions explicitly account for any requirement contained in the standards and guidelines. .\n#### 4. Artificial intelligence and machine learning readiness of national oceanic and atmospheric administration data assets for operational forecasting\n##### (a) In general\nAfter the adoption by the Under Secretary of Commerce for Oceans and Atmosphere (in this section referred to as the Under Secretary ) of the standards and guidelines described in section 701 of the National Science and Technology Policy, Organization, and Priorities Act of 1976, as added by section 3, the Under Secretary shall ensure the data assets of the National Oceanic and Atmospheric Administration (in this section referred to as the Administration ) support the integration of artificial intelligence and machine learning into the operational forecasting activities of the Administration, specifically for\u2014\n**(1)**\nmodel analyses, forecasts, and reanalyses;\n**(2)**\nin-situ and conventional observations;\n**(3)**\nsatellite datasets; and\n**(4)**\nenvironmental observations that are critical for forecasting.\n##### (b) Annual briefings\nNot later than 1 year after the date of adoption described in subsection (a), and annually thereafter for 5 years, the Under Secretary shall brief the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives on the progress made by the Under Secretary in implementing subsection (a).",
      "versionDate": "2026-03-16",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-03-31T20:34:49Z"
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
      "date": "2026-03-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4098is.xml"
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
      "title": "A bill to establish standards and guidelines to make open Government data assets artificial intelligence-ready, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T05:18:36Z"
    },
    {
      "title": "Artificial Intelligence-Ready Data Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Artificial Intelligence-Ready Data Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T05:08:19Z"
    }
  ]
}
```
