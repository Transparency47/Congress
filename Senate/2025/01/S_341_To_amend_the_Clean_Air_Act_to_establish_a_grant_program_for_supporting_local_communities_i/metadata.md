# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/341?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/341
- Title: Smoke and Heat Ready Communities Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 341
- Origin chamber: Senate
- Introduced date: 2025-01-30
- Update date: 2025-12-05T21:49:58Z
- Update date including text: 2025-12-05T21:49:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-30: Introduced in Senate
- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-01-30: Introduced in Senate

## Actions

- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-30",
    "latestAction": {
      "actionDate": "2025-01-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/341",
    "number": "341",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Smoke and Heat Ready Communities Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:49:58Z",
    "updateDateIncludingText": "2025-12-05T21:49:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-30",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-30",
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
          "date": "2025-01-30T21:09:54Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "CT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "CA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "CA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "OR"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernard",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-01-30",
      "state": "VT"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "CO"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s341is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 341\nIN THE SENATE OF THE UNITED STATES\nJanuary 30, 2025 Mr. Merkley (for himself, Mr. Blumenthal , Mr. Padilla , Mr. Schiff , Mr. Wyden , Mr. Sanders , and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Clean Air Act to establish a grant program for supporting local communities in detecting, preparing for, communicating about, or mitigating the environmental and public health impacts of wildfire smoke and extreme heat, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Smoke and Heat Ready Communities Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means Administrator of the Environmental Protection Agency.\n**(2) Extreme heat**\nThe term extreme heat has the meaning given the term through a rulemaking of the Administrator, in consultation with the heads of relevant Federal agencies.\n**(3) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(4) Native Hawaiian organization**\nThe term Native Hawaiian organization has the meaning given the term in section 6207 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7517 ).\n#### 3. Smoke and extreme heat-ready communities\nPart A of title I of the Clean Air Act ( 42 U.S.C. 7401 et seq. ) is amended by adding at the end the following:\n139. Smoke and extreme heat-ready communities (a) Definition of extreme heat The term extreme heat has the meaning given the term in section 2 of the Smoke and Heat Ready Communities Act of 2025 . (b) Establishment Subject to the availability of appropriations, the Administrator may make grants under this section to air pollution control agencies to support air pollution control agencies in developing and implementing programs that support local communities in detecting, preparing for, communicating with the public about, or mitigating the environmental and public health aspects of wildfire smoke and extreme heat. (c) Eligible activities In carrying out a program described in subsection (b), an air pollution control agency may use funds from a grant received under this section for\u2014 (1) activities related to the monitoring of, the interpretation of, and communicating with the public about past, present, and future data related to ambient air quality conditions that are caused by wildfire smoke and extreme heat; (2) conducting community outreach in areas that may be prone to poor air quality that is attributable to elevated levels of particulate matter, ozone, and other harmful components of wildfire smoke and extreme heat; (3) the deployment of air quality monitoring equipment in a manner that is sufficient to evaluate an increased prevalence of poor air quality that is attributable to elevated levels of particulate matter, ozone, and other harmful components of wildfire smoke and extreme heat; (4) equipping public buildings with air filtration systems that are capable of removing particulate matter and other harmful components of wildfire smoke and extreme heat from the air so that the public buildings may serve as cleaner air spaces during wildfire smoke events and extreme heat events and other poor air quality events; (5) the purchase, storage, and distribution of face masks and personal protective equipment, including N\u201395 filtering facepiece respirators, portable air filtration systems, and other masks and equipment that are capable of removing or otherwise preventing the inhalation of particulate matter, ozone, and other harmful components of wildfire smoke and extreme heat from the air; (6) subgrants or providing other financing to private or other public entities with demonstrated financial need\u2014 (A) to acquire protective gear; or (B) to carry out weatherization measures to mitigate air infiltration; and (7) such other activities that the Administrator determines to be necessary to carry out the purposes of this section. (d) Allocation of funds (1) In general Subject to paragraph (2), the Administrator shall establish a formula to distribute grants under this section among air pollution control agencies. (2) Considerations In establishing the formula required under paragraph (1), the Administrator shall consider\u2014 (A) the vulnerability of communities within a State to wildfire smoke and extreme heat; and (B) the degree to which a State is prone to poor air quality that is attributable to elevated levels of particulate matter from wildfire smoke and extreme heat. (e) Authorization of appropriations There are authorized to be appropriated such sums as are necessary to carry out this section. .\n#### 4. Research on wildfire smoke and extreme heat\n##### (a) Centers of excellence\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Administrator shall establish at institutions of higher education (as defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) )) 4 centers, each of which shall be known as a Center of Excellence for Wildfire Smoke and Extreme Heat , to carry out research relating to\u2014\n**(A)**\nthe effects on public health, including the health of outdoor workers, of\u2014\n**(i)**\nsmoke emissions from wildland fires; and\n**(ii)**\nextreme heat; and\n**(B)**\nmeans by which communities can better respond to the impacts of\u2014\n**(i)**\nemissions from wildland fires; and\n**(ii)**\nextreme heat events.\n**(2) Priority**\nIn selecting institutions of higher education (as so defined) at which to establish a center under paragraph (1), the Administrator shall give priority to institutions of higher education (as so defined) that\u2014\n**(A)**\nhave established expertise with respect to air quality or dedicated centers of air quality research;\n**(B)**\nhave experience with relevant outreach and extension work;\n**(C)**\nhave established relationships with relevant Federal, State, and local agencies, community organizations, Native Hawaiian organizations, and Indian Tribes; and\n**(D)**\nare located in an area that is economically or environmentally impacted by wildfire smoke or extreme heat.\n**(3) Authorization of appropriations**\nThere is authorized to be appropriated to the Administrator to carry out this subsection $10,000,000 for fiscal year 2026 and each fiscal year thereafter.\n##### (b) Research\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Administrator shall begin to carry out research\u2014\n**(A)**\nto study the health effects of\u2014\n**(i)**\nsmoke emissions from wildland fires; and\n**(ii)**\nextreme heat;\n**(B)**\nto develop and disseminate personal and community-based interventions to reduce exposure to and adverse health effects of\u2014\n**(i)**\nsmoke emissions from wildland fires; and\n**(ii)**\nextreme heat;\n**(C)**\nto increase the quality of smoke and extreme heat monitoring and prediction tools and techniques; and\n**(D)**\nto develop implementation and communication strategies.\n**(2) Authorization of appropriations**\nThere is authorized to be appropriated to the Administrator to carry out this subsection $20,000,000 for fiscal year 2026 and each fiscal year thereafter.\n#### 5. Community smoke and extreme heat planning\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Administrator shall establish a competitive grant program to assist eligible entities described in subsection (b) in developing and implementing collaborative community plans for mitigating the impacts of smoke emissions from wildland fires and extreme heat.\n##### (b) Eligible entities\nAn entity that is eligible to submit an application for a grant under subsection (a) is\u2014\n**(1)**\na State;\n**(2)**\na unit of local government (including any special district, such as an air quality management district or a school district);\n**(3)**\nan Indian Tribe; or\n**(4)**\na Native Hawaiian organization.\n##### (c) Applications\nTo be eligible to receive a grant under subsection (a), an eligible entity described in subsection (b) shall submit to the Administrator an application at such time, in such manner, and containing such information as the Administrator may require, which shall include a plan to collaborate with a public institution of higher education (as defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) )) or other research institution that\u2014\n**(1)**\nhas established expertise with respect to air quality or dedicated centers of air quality research;\n**(2)**\nhas experience with relevant outreach and extension work;\n**(3)**\nhas established relationships with relevant Federal, State, and local agencies, community organizations, Native Hawaiian organizations, and Indian Tribes; and\n**(4)**\nis located in an area that is economically or environmentally impacted by wildfire smoke or extreme heat.\n##### (d) Technical assistance\nThe Administrator may use amounts made available to carry out this section to provide to eligible entities described in subsection (b) technical assistance in\u2014\n**(1)**\nsubmitting grant applications under subsection (c); or\n**(2)**\ncarrying out projects using a grant under this section.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated to the Administrator to carry out this section $50,000,000 for fiscal year 2026 and each fiscal year thereafter.",
      "versionDate": "2025-01-30",
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
        "actionDate": "2025-01-31",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "903",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Smoke and Heat Ready Communities Act of 2025",
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
        "name": "Environmental Protection",
        "updateDate": "2025-03-07T13:01:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-30",
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
          "measure-id": "id119s341",
          "measure-number": "341",
          "measure-type": "s",
          "orig-publish-date": "2025-01-30",
          "originChamber": "SENATE",
          "update-date": "2025-03-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s341v00",
            "update-date": "2025-03-18"
          },
          "action-date": "2025-01-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Smoke and Heat Ready Communities Act of 2025</strong></p><p>This bill authorizes the Environmental Protection Agency (EPA) to make grants to air pollution control agencies to support the development and implementation of programs that support local communities in detecting, preparing for, communicating with the public about, or mitigating the environmental and public health aspects of wildfire smoke and extreme heat. The EPA must establish a formula to distribute the grants among air pollution control agencies.</p><p>The bill requires the EPA to establish four Centers of Excellence for Wildfire Smoke and Extreme Heat at institutions of higher education to research (1) the effects of smoke emissions from wildland fires and extreme heat on public health, and (2) the means by which communities can better respond to impacts from such conditions.</p><p>Additionally, the EPA must begin to carry out research to</p><ul><li>study the health effects of smoke emissions from wildland fires and extreme heat;</li><li>develop and disseminate personal and community-based interventions to reduce exposure to, and health effects of, wildland fire smoke emissions and extreme heat;</li><li>increase the quality of smoke and extreme heat monitoring and prediction tools and techniques; and</li><li>develop implementation and communication strategies.</li></ul><p>The EPA must also establish a competitive grant program to assist certain entities (e.g., a state) in developing and implementing collaborative community plans for mitigating the impacts of smoke emissions from wildland fires and extreme heat.</p>"
        },
        "title": "Smoke and Heat Ready Communities Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s341.xml",
    "summary": {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Smoke and Heat Ready Communities Act of 2025</strong></p><p>This bill authorizes the Environmental Protection Agency (EPA) to make grants to air pollution control agencies to support the development and implementation of programs that support local communities in detecting, preparing for, communicating with the public about, or mitigating the environmental and public health aspects of wildfire smoke and extreme heat. The EPA must establish a formula to distribute the grants among air pollution control agencies.</p><p>The bill requires the EPA to establish four Centers of Excellence for Wildfire Smoke and Extreme Heat at institutions of higher education to research (1) the effects of smoke emissions from wildland fires and extreme heat on public health, and (2) the means by which communities can better respond to impacts from such conditions.</p><p>Additionally, the EPA must begin to carry out research to</p><ul><li>study the health effects of smoke emissions from wildland fires and extreme heat;</li><li>develop and disseminate personal and community-based interventions to reduce exposure to, and health effects of, wildland fire smoke emissions and extreme heat;</li><li>increase the quality of smoke and extreme heat monitoring and prediction tools and techniques; and</li><li>develop implementation and communication strategies.</li></ul><p>The EPA must also establish a competitive grant program to assist certain entities (e.g., a state) in developing and implementing collaborative community plans for mitigating the impacts of smoke emissions from wildland fires and extreme heat.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119s341"
    },
    "title": "Smoke and Heat Ready Communities Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Smoke and Heat Ready Communities Act of 2025</strong></p><p>This bill authorizes the Environmental Protection Agency (EPA) to make grants to air pollution control agencies to support the development and implementation of programs that support local communities in detecting, preparing for, communicating with the public about, or mitigating the environmental and public health aspects of wildfire smoke and extreme heat. The EPA must establish a formula to distribute the grants among air pollution control agencies.</p><p>The bill requires the EPA to establish four Centers of Excellence for Wildfire Smoke and Extreme Heat at institutions of higher education to research (1) the effects of smoke emissions from wildland fires and extreme heat on public health, and (2) the means by which communities can better respond to impacts from such conditions.</p><p>Additionally, the EPA must begin to carry out research to</p><ul><li>study the health effects of smoke emissions from wildland fires and extreme heat;</li><li>develop and disseminate personal and community-based interventions to reduce exposure to, and health effects of, wildland fire smoke emissions and extreme heat;</li><li>increase the quality of smoke and extreme heat monitoring and prediction tools and techniques; and</li><li>develop implementation and communication strategies.</li></ul><p>The EPA must also establish a competitive grant program to assist certain entities (e.g., a state) in developing and implementing collaborative community plans for mitigating the impacts of smoke emissions from wildland fires and extreme heat.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119s341"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s341is.xml"
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
      "title": "Smoke and Heat Ready Communities Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-03T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Smoke and Heat Ready Communities Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Clean Air Act to establish a grant program for supporting local communities in detecting, preparing for, communicating about, or mitigating the environmental and public health impacts of wildfire smoke and extreme heat, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:29Z"
    }
  ]
}
```
