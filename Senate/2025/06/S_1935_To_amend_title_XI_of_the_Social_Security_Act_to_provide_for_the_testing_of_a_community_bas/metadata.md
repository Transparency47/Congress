# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1935?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1935
- Title: Expanding Access to Palliative Care Act
- Congress: 119
- Bill type: S
- Bill number: 1935
- Origin chamber: Senate
- Introduced date: 2025-06-03
- Update date: 2026-01-07T12:03:26Z
- Update date including text: 2026-01-07T12:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-03: Introduced in Senate
- 2025-06-03 - IntroReferral: Introduced in Senate
- 2025-06-03 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-03: Introduced in Senate

## Actions

- 2025-06-03 - IntroReferral: Introduced in Senate
- 2025-06-03 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-03",
    "latestAction": {
      "actionDate": "2025-06-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1935",
    "number": "1935",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacky",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Expanding Access to Palliative Care Act",
    "type": "S",
    "updateDate": "2026-01-07T12:03:26Z",
    "updateDateIncludingText": "2026-01-07T12:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-03",
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
      "actionDate": "2025-06-03",
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
            "date": "2025-06-03T19:28:13Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-03T19:28:13Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "WY"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "WI"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "NE"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1935is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1935\nIN THE SENATE OF THE UNITED STATES\nJune 3, 2025 Ms. Rosen (for herself, Mr. Barrasso , Ms. Baldwin , and Mrs. Fischer ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XI of the Social Security Act to provide for the testing of a community-based palliative care model.\n#### 1. Short title\nThis Act may be cited as the Expanding Access to Palliative Care Act .\n#### 2. Community-based palliative care model\nSection 1115A of the Social Security Act ( 42 U.S.C. 1315a ) is amended\u2014\n**(1)**\nin subsection (b)(2)(A), by adding at the end the following new sentence: The models selected under this subparagraph shall include the testing of the model described in subsection (h). ; and\n**(2)**\nby adding at the end the following new subsection:\n(h) Community-Based palliative care model (1) In general The CMI shall develop and implement a model to provide community-based palliative care and care coordination for high-risk beneficiaries, in co-management with other providers of services and suppliers, aimed at improving outcomes and experience of care and reducing unnecessary or unwanted emergency department visits and hospitalizations (in this subsection referred to as the model ), and that is intended to replace the Medicare Care Choices Model. (2) Duration The model shall be implemented for a 5-year period, beginning not later than one year after the date of the enactment of this subsection. (3) Target population (A) In general The target population for the model is an individual\u2014 (i) entitled to, or enrolled for, benefits under part A of title XVIII; and (ii) with a diagnosis of a serious illness or injury, which may include a diagnosis of cancer, heart and vascular disease, pulmonary disease, human immunodeficiency virus/acquired immunodeficiency, Alzheimer\u2019s and dementia, stroke, serious injury requiring rehabilitation including burns, kidney disease, liver disease, Amyotrophic lateral sclerosis, any neuro degenerative disease, or any other serious illness or injury the Secretary determines appropriate. (B) No exclusion for prior use of hospice care benefits An individual shall not be excluded from participation in the model based on prior use of hospice care benefits during any period prior to such participation, regardless of the source of coverage for such benefits. (4) Participating providers Providers eligible to participate under the model may include palliative care teams working as an independent practice or associated with a hospice program, home health agencies, hospitals, integrated health systems, and other facilities determined appropriate by the Secretary. (5) Team-based approach Under the model, at least one member of the multi-disciplinary palliative care team shall be certified in hospice and palliative care. This is a co-management model with palliative care aligning with primary and specialist care for a team-based approach. Care must be coordinated across providers and community services for inclusion of all pain, symptom management, disease-modifying and curative treatments, and other palliative care services. (6) Location Care may be furnished under the model in any beneficiary home , including a caregiver\u2019s residence, an extended care facility, or a community setting as appropriate based on the individual's ability to access services. The model shall include access within an in-patient stay so long as the patient begins receiving palliative care services prior to admission. Services shall not be disrupted solely due to change in location from a residence to an in-patient setting, and shall be part of care coordination and care planning following hospital discharge. (7) Services The model shall include items and services based on specific patient needs with respect to pain, symptom management, education, disease modifying treatments, advance care planning and shared decision making, goals clarification, mental health services, family and caregiver support services, spiritual support care, personal care assistance, and stress reduction therapies. This includes a comprehensive assessment of symptoms and stress factors that impact quality of life. (8) Access Care shall be available under the model 24 hours a day, 7 days a week, and 365 days a year, including telehealth services. The CMI shall specifically consider the needs of rural and underserved areas and adjust accordingly to ensure equitable access to care. A broad range of providers must be included with no geographic limitations. (9) Metrics The CMI shall assess the model by comparing participants to other members of the target population who are receiving care outside of the model, including with respect to the following: (A) Demographics (including age, diagnosis, residence type, medical encounters in preceding 12 months leading to enrollment, geographic location (such as urban or rural) and others as determined by the CMI). (B) Impact on utilization of items and services under title XVIII (such as emergency department services, hospital observation services, inpatient admissions, and intensive care unit (ICU) stays). (C) Election of hospice care. (D) Duration of hospice care. (E) Care Experience (beneficiary and caregiver). .",
      "versionDate": "2025-06-03",
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
        "name": "Health",
        "updateDate": "2025-06-23T14:13:11Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-03",
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
          "measure-id": "id119s1935",
          "measure-number": "1935",
          "measure-type": "s",
          "orig-publish-date": "2025-06-03",
          "originChamber": "SENATE",
          "update-date": "2025-07-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1935v00",
            "update-date": "2025-07-25"
          },
          "action-date": "2025-06-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Expanding Access to Palliative Care Act</b></p> <p>This bill requires the Center for Medicare and Medicaid Innovation (CMMI) to test a model that provides community-based palliative care and care coordination for high-risk Medicare beneficiaries and that may replace the Medicare Care Choices Model (which ended on December 31, 2021). </p> <p>Under the new model, multi-disciplinary teams must provide coordinated, palliative care that is available 24-7 for Medicare beneficiaries with serious illnesses or injuries, such as cancer. The CMMI must evaluate the model by comparing patients participating in the model with those outside of the model in relation to specified metrics, including the election and duration of hospice care.</p>"
        },
        "title": "Expanding Access to Palliative Care Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1935.xml",
    "summary": {
      "actionDate": "2025-06-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Expanding Access to Palliative Care Act</b></p> <p>This bill requires the Center for Medicare and Medicaid Innovation (CMMI) to test a model that provides community-based palliative care and care coordination for high-risk Medicare beneficiaries and that may replace the Medicare Care Choices Model (which ended on December 31, 2021). </p> <p>Under the new model, multi-disciplinary teams must provide coordinated, palliative care that is available 24-7 for Medicare beneficiaries with serious illnesses or injuries, such as cancer. The CMMI must evaluate the model by comparing patients participating in the model with those outside of the model in relation to specified metrics, including the election and duration of hospice care.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s1935"
    },
    "title": "Expanding Access to Palliative Care Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Expanding Access to Palliative Care Act</b></p> <p>This bill requires the Center for Medicare and Medicaid Innovation (CMMI) to test a model that provides community-based palliative care and care coordination for high-risk Medicare beneficiaries and that may replace the Medicare Care Choices Model (which ended on December 31, 2021). </p> <p>Under the new model, multi-disciplinary teams must provide coordinated, palliative care that is available 24-7 for Medicare beneficiaries with serious illnesses or injuries, such as cancer. The CMMI must evaluate the model by comparing patients participating in the model with those outside of the model in relation to specified metrics, including the election and duration of hospice care.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s1935"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1935is.xml"
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
      "title": "Expanding Access to Palliative Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-07T12:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Expanding Access to Palliative Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-10T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XI of the Social Security Act to provide for the testing of a community-based palliative care model.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-10T02:48:17Z"
    }
  ]
}
```
