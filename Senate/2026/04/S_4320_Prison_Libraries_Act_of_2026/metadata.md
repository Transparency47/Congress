# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4320?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4320
- Title: Prison Libraries Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4320
- Origin chamber: Senate
- Introduced date: 2026-04-16
- Update date: 2026-05-12T20:36:52Z
- Update date including text: 2026-05-12T20:36:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in Senate
- 2026-04-16 - IntroReferral: Introduced in Senate
- 2026-04-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-04-16: Introduced in Senate

## Actions

- 2026-04-16 - IntroReferral: Introduced in Senate
- 2026-04-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4320",
    "number": "4320",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Prison Libraries Act of 2026",
    "type": "S",
    "updateDate": "2026-05-12T20:36:52Z",
    "updateDateIncludingText": "2026-05-12T20:36:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-16",
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
      "actionDate": "2026-04-16",
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
          "date": "2026-04-16T17:00:56Z",
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
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "IL"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "HI"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "CA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4320is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4320\nIN THE SENATE OF THE UNITED STATES\nApril 16 (legislative day, April 14), 2026 Mr. Schiff (for himself, Mr. Durbin , Ms. Hirono , Mr. Padilla , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo establish a program to make grants for the establishment of prison libraries.\n#### 1. Short title\nThis Act may be cited as the Prison Libraries Act of 2026 .\n#### 2. Establishment\nNot later than 1 year after the date of enactment of this Act, the Attorney General shall establish a program to make grants to eligible applicants for the purpose of providing library services to incarcerated individuals in order to advance reintegration efforts, reduce recidivism, and increase educational opportunities.\n#### 3. Eligibility criteria\nAn eligible grantee under this Act is any State or territory that submits an application that includes the following:\n**(1)**\nA comprehensive plan for how the grant will be used, including project objectives, program design, and evaluation process.\n**(2)**\nProof of the existence of a physical library at a correctional facility or the intention of creating one.\n**(3)**\nData on the demographics of the population of the facility sufficient to demonstrate a compelling need for funding, including educational level of prison population, rates of recidivism, socioeconomic breakdown of the prison population or any other relevant data.\n#### 4. Use of funds\nGrant amounts shall be used to provide library services to incarcerated individuals as set forth in section 2, and may include usage for any of the following:\n**(1)**\nEducation and job training.\n**(2)**\nAcquisition of modern materials and equipment that reflect the interests, identities, abilities, and languages of the prison population.\n**(3)**\nExpansion of the infrastructure of prison libraries to be less restrictive, safety permitted, and more welcoming with design and decor.\n**(4)**\nHiring of qualified librarians and staff to manage the libraries, their resources, and services and serve as the social coordinator for organized activities and events, and who hold the following qualifications:\n**(A)**\nHave practical library management experience.\n**(B)**\nDemonstrated ability to catalogue, archive, and maintain databases and E-resources.\n**(C)**\nDemonstrated ability to organize weekly, bi-weekly, and monthly events and activities.\n**(5)**\nLiterary training.\n**(6)**\nDigital literacy training.\n**(7)**\nCareer readiness programming.\n**(8)**\nCivic engagement programs.\n**(9)**\nRestorative justice programs.\n**(10)**\nResident-led programs.\n**(11)**\nHealth and wellness activities.\n**(12)**\nCultural exchange and appreciation programs, events, and activities.\n**(13)**\nAccess to computers (including laptops) and the internet.\n**(14)**\nBook discussion programs.\n**(15)**\nLanguage services, including free English classes.\n**(16)**\nAudiobooks and accessible reading materials for the visually impaired and print disabled.\n**(17)**\neBooks.\n**(18)**\nManagement of book donation programs.\n**(19)**\nAudio and visual materials or multimedia.\n**(20)**\nArtistic programing such as painting, creative writing, poetry slams, drama, or music.\n**(21)**\nFinancial literacy.\n**(22)**\nFamily literacy activities facilitated during in-person visits.\n**(23)**\nResource fairs.\n**(24)**\nMaking reasonable efforts toward building a working relationship with local public libraries, including\u2014\n**(A)**\nadoption of a standardized guideline for library management;\n**(B)**\nsharing of resources and materials through an interlibrary loan arrangement; and\n**(C)**\nimplementation of coordinated organized events and activities.\n#### 5. Prohibited uses\nGrant amounts may not be used for the following:\n**(1)**\nPurchasing food, clothes, shoes, or hygiene supplies.\n**(2)**\nPayment of employee salary and benefits unassociated with prison libraries.\n**(3)**\nPhysical and mental care for incarcerated individuals.\n**(4)**\nIncarcerated individual transportation.\n**(5)**\nStaff training unrelated to library services.\n**(6)**\nGeneral administrative functions or operations of the prison.\n**(7)**\nFacility maintenance unrelated to the libraries.\n**(8)**\nOther obligations imposed on the facility by law, including establishment of maintenance of a law library.\n**(9)**\nAny other use unrelated to library services, resources, and management.\n#### 6. Prioritization\nThe Attorney General shall, in making grants under this Act, comply with the following:\n**(1)**\nThe Attorney General shall prioritize making awards to grantees that are the following:\n**(A)**\nApplicants that follow local or national standards and guidelines for library management.\n**(B)**\nApplicants that add or prioritize post-secondary education curriculum to library programming.\n**(C)**\nApplicants with plans for tangible, positive, and measurable impact for their prison population, including\u2014\n**(i)**\nplans for increasing literacy rates;\n**(ii)**\nplans for increased secondary and post-secondary enrollment and graduation rates;\n**(iii)**\nplans for development of technical and vocational skills;\n**(iv)**\nplans for expanded access to employment opportunities post-release; and\n**(v)**\nany other factors that the Attorney General determines appropriate.\n**(D)**\nApplicants with plans for numerous initiatives to maximize benefits and services for their prison population.\n**(2)**\nThe Attorney General shall ensure geographic diversity as between grantees with regard to the States and territories and between urban and rural areas.\n**(3)**\nThe Attorney General shall establish a reporting system to monitor progress, performance, and expenditures of grantees.\n#### 7. Term\nA grant under this Act shall be for a term of 1 year, and may be renewed annually for a period of not more than 6 years in total.\n#### 8. Reporting\nGrantees shall submit annual performance measures, including library activity statistics and program outcomes, and expenditure reports to systems established by the Attorney General under section 6(3).\n#### 9. Conditions\n##### (a) In general\nA grantee may not charge a fee to any incarcerated individual for the following:\n**(1)**\nAccess to physical books.\n**(2)**\nAccess to eBooks and audiobooks.\n**(3)**\nAccess to computers (including laptops) and the internet within the library.\n**(4)**\nAccess to educational and artistic materials needed to facilitate learning, training, or activities, including notebooks, pens, pencils, paints, and similar supplies.\n**(5)**\nPrinting services.\n**(6)**\nAny other library services or resources.\n##### (b) Availability for educational programming\nA grantee shall make the library space available to post-secondary organizations and personnel for educational programming.\n#### 10. Consultation\nThe Attorney General shall consult with the Director of the Institute of Museum and Library Services in implementing this Act.\n#### 11. Authorization of appropriations\nThere are authorized to be appropriated to carry out this Act $10,000,000 for each of fiscal years 2026 through 2031.",
      "versionDate": "2026-04-16",
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
        "actionDate": "2026-01-27",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "7247",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Prison Libraries Act of 2026",
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
        "updateDate": "2026-05-12T20:36:52Z"
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
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4320is.xml"
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
      "title": "Prison Libraries Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T04:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Prison Libraries Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a program to make grants for the establishment of prison libraries.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-30T04:48:39Z"
    }
  ]
}
```
