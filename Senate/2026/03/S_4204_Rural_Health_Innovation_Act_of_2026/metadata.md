# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4204?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4204
- Title: Rural Health Innovation Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4204
- Origin chamber: Senate
- Introduced date: 2026-03-25
- Update date: 2026-04-14T13:50:32Z
- Update date including text: 2026-04-14T13:50:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in Senate
- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-03-25: Introduced in Senate

## Actions

- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4204",
    "number": "4204",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Rural Health Innovation Act of 2026",
    "type": "S",
    "updateDate": "2026-04-14T13:50:32Z",
    "updateDateIncludingText": "2026-04-14T13:50:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
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
      "actionDate": "2026-03-25",
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
          "date": "2026-03-25T22:24:57Z",
          "name": "Referred To"
        }
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
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CO"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4204is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4204\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2026 Mrs. Blackburn (for herself, Mr. Hickenlooper , and Mrs. Hyde-Smith ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to establish a rural health center innovation awards program and a rural health department enhancement program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Health Innovation Act of 2026 .\n#### 2. Rural health center innovation awards program\nSubpart I of part D of title III of the Public Health Service Act ( 42 U.S.C. 254b et seq. ) is amended by adding at the end the following:\n330Q. Rural health center innovation awards program (a) Definitions In this section: (1) Eligible entity The term eligible entity means an entity that\u2014 (A) is a Federally qualified health center; (B) is a rural health clinic; or (C) agrees (as a condition of receiving a grant under this section) to establish such a center or clinic, including a hospital that agrees (as such a condition) to convert to a Federally qualified health center or rural health clinic. (2) Federally qualified health center The term Federally qualified health center has the meaning given such term in section 1861(aa) of the Social Security Act. (3) Rural health clinic The term rural health clinic has the meaning given such term in section 1861(aa) of the Social Security Act. (b) Establishment (1) In general The Secretary, acting through the Director of the Office of Rural Health Policy of the Health Resources and Services Administration, shall establish a grant program to be known as the Rural Health Center Innovation Awards program to award grants to eligible entities that submit an application in accordance with subsection (c) to enable such entities to establish or maintain a Federally qualified health center or rural health clinic that\u2014 (A) serves individuals in a rural area as a walk-in urgent care center and as a triage center or staging facility for necessary air or ambulance transport to an emergency department; and (B) includes\u2014 (i) professional clinical staff, including physicians, physician interns, residents, nurse practitioners, physician assistants, nurse midwives, or other health care providers providing walk-in urgent care and emergency triage; and (ii) resources, including laboratories, x-ray machines, and cardiac monitors. (2) Permissible uses of funds The funds of a grant awarded under this section may be used to\u2014 (A) expand the hours of operation of a Federally qualified health center or rural health clinic; (B) pay for the costs of construction and renovation of a Federally qualified health center or rural health clinic; or (C) carry out any other activity for the purposes described in paragraph (1). (c) Applications and selection (1) In general An eligible entity seeking a grant under this section shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may reasonably require. (2) Start up centers and clinics An application submitted under paragraph (1) by an eligible entity that is not a Federally qualified health center, or a rural health clinic, on the date on which the entity submits the application under paragraph (1) shall include in such application a demonstration of the costs of the equipment and staffing needed to establish the center or clinic. (3) Consideration of overlap In the case an eligible entity submits an application under paragraph (1) that proposes to serve an area that is served by another eligible entity through a grant under this section, the Secretary may consider whether an award to the eligible entity serving such same area can be justified based on the unmet need for additional services in such area. (4) Priority In selecting recipients of grants under this section, the Secretary shall give priority to an eligible entity that is operating as a Federally qualified health center, or a rural health clinic, on the date on which the entity submits the application under paragraph (1). (d) Grant period and amounts (1) Period Each grant awarded under this section shall be for a period of 5 years. (2) Amount (A) In general A grant awarded under this section to an eligible entity shall not exceed\u2014 (i) for the first year of the grant\u2014 (I) $500,000 if the entity is a Federally qualified health center, or a rural health clinic, on the date on which the award is made; and (II) $750,000 if the entity is using the grant to establish a Federally qualified health center or a rural health clinic; and (ii) for each of the second through fifth years of the grant, $500,000. (B) Considerations In determining the amount of a grant under this section for an eligible entity for each year after the first year in which the grant is awarded, the Secretary shall, subject to subparagraph (A)(ii), consider the number of patients treated, and the type of treatment provided, by the entity in the prior year. (e) Reporting (1) In general Not later than 3 years after the date of enactment of this section, the Secretary shall report to the committees described in paragraph (2) on the grant program under this section, including\u2014 (A) an assessment of the success of the program, challenges with respect to the program, and any action for regulatory flexibility or legislative authority needed to improve the program; (B) any savings to Federal health care programs; (C) any increase in access to care; and (D) any increase in utilization of health services in rural areas. (2) Committees The committees described in this paragraph are\u2014 (A) the Committee on Health, Education, Labor, and Pensions, and the Committee on Finance, of the Senate; and (B) the Committee on Energy and Commerce, and the Committee on Ways and Means, of the House of Representatives. (f) Rule of construction No entity receiving a grant under this section shall lose status as a Federally qualified health center, or a rural health clinic, on account of carrying out any activities under this section. (g) Authorization of appropriations There is authorized to be appropriated to carry out this section $25,000,000 for each of fiscal years 2027 through 2031. .\n#### 3. Rural health department enhancement program\nSubpart I of part D of title III of the Public Health Service Act ( 42 U.S.C. 254b et seq. ), as amended by section 2, is further amended by adding at the end the following:\n330R. Rural health department enhancement program (a) Definition of rural health department In this section, the term rural health department means a local public health department that is located in a rural area. (b) Establishment The Secretary, acting through the Director of the Office of Rural Health Policy of the Health Resources and Services Administration, shall award grants, on a competitive basis, to rural health departments that submit an application in accordance with subsection (c) to enhance such departments and enable them to provide individuals in rural areas with emergency services, triage and transport to emergency departments, primary care services, and other services similar to services provided by emergency departments. (c) Applications A rural health department seeking a grant under this section shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may reasonably require, including\u2014 (1) an indication of the estimated cost of the equipment and staffing needed by the department for the first year of the award to set up the activities and services under this section; (2) a demonstration that the department has, on the date on which the application is submitted, a facility operating that is located in a rural area; and (3) a demonstration that, on the date on which the application is submitted, the department\u2014 (A) has a nursing staff and medical equipment; and (B) agrees to use such staff and equipment towards providing the services and carrying out the activities under this section. (d) Grants (1) Annual awards The funds awarded through a grant under this section to a rural health department shall be awarded on an annual basis for each of 5 years. (2) Maximum amounts The funds awarded through a grant under this section to a rural health department shall be in an amount that for a year does not exceed $500,000. (3) Considerations The Secretary shall determine the amount awarded to a rural health department through a grant under this section for a year in accordance with the following: (A) For the first year of the award, the amount shall be based on the amount the rural health department estimates for the cost of equipment and staffing needed to set up the activities and services supported under this section, as specified in the application under subsection (c). (B) For the second through fifth years of the award, the amount shall be based on the number of patients treated, and the type of treatment provided, by the department in the prior year. (e) Use of funds (1) In general A rural health department receiving a grant under this section shall use the funds awarded through the grant to provide the services and carry out the activities described in subsection (b) at a facility that is located in a rural area, including by\u2014 (A) obtaining additional medical equipment and resources necessary for providing the services and activities described in subsection (b), such as laboratories, x-ray machines, and cardiac monitors; (B) hiring additional providers to provide the services and carry out the activities described in subsection (b), such as physician interns, residents, nurse practitioners, physician assistants, and nurse midwives, which hiring may be through a partnership described in paragraph (2)(A); and (C) providing outreach to the community regarding the services and activities of the rural health department as supported under this section. (2) Limitations (A) Partnerships Not more than 3 percent of the funds awarded through a grant under this section for a year may be used towards the rural health department entering into a partnership with an academic medical center to assist with the hiring described in paragraph (1)(B). (B) Community outreach For each of the first 2 years of a grant awarded under this section, not more than 3 percent of the funds may be used by the rural health department receiving the grant for the outreach described in paragraph (1)(C). (f) Authorization of appropriations There are authorized to be appropriated to carry out this section $25,000,000 for each of fiscal years 2027 through 2031. .",
      "versionDate": "2026-03-25",
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
        "actionDate": "2025-02-21",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1480",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Rural Health Innovation Act of 2025",
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
        "name": "Health",
        "updateDate": "2026-04-13T16:16:15Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4204is.xml"
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
      "title": "Rural Health Innovation Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-10T02:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rural Health Innovation Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-10T02:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to establish a rural health center innovation awards program and a rural health department enhancement program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-10T02:33:20Z"
    }
  ]
}
```
