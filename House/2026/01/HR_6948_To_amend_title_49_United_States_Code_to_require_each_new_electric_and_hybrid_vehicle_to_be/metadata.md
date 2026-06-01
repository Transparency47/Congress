# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6948?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6948
- Title: To amend title 49, United States Code, to require each new electric and hybrid vehicle to be equipped with technology that allows the timely extinguishment of an electric vehicle battery fire, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 6948
- Origin chamber: House
- Introduced date: 2026-01-06
- Update date: 2026-01-22T16:04:10Z
- Update date including text: 2026-01-22T16:04:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-06: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-01-06: Introduced in House

## Actions

- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-06",
    "latestAction": {
      "actionDate": "2026-01-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6948",
    "number": "6948",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "L000606",
        "district": "16",
        "firstName": "George",
        "fullName": "Rep. Latimer, George [D-NY-16]",
        "lastName": "Latimer",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "To amend title 49, United States Code, to require each new electric and hybrid vehicle to be equipped with technology that allows the timely extinguishment of an electric vehicle battery fire, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-01-22T16:04:10Z",
    "updateDateIncludingText": "2026-01-22T16:04:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-06",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-06",
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
          "date": "2026-01-06T23:30:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6948ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6948\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 6, 2026 Mr. Latimer (for himself and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title 49, United States Code, to require each new electric and hybrid vehicle to be equipped with technology that allows the timely extinguishment of an electric vehicle battery fire, and for other purposes.\n#### 1. Electric and hybrid vehicle standards\n##### (a) Electric and hybrid vehicles\nSubchapter II of chapter 301 of title 49, United States Code, is amended by adding at the end the following new section:\n30130 Electric and hybrid vehicles (a) Battery safety (1) In general Not later than 2 years after the date of the enactment of this section, the Secretary shall promulgate a final motor vehicle standard to mitigate unreasonable risk of fire, explosion, reignition, stranded energy, thermal runaway, fire breaching the passenger compartment, loss of electrical power, and any other safety risk related to the battery used in any new electric or new hybrid vehicle manufactured for sale, sold, offered for sale, or introduced or delivered for introduction in interstate commerce in the United States. (2) Consultation The Secretary shall promulgate such standard in consultation with a representative from each of the following: (A) Major electric vehicle and hybrid vehicle manufacturers. (B) An accredited standards development organization with expertise in fire protection. (C) An organization that represents professional firefighters. (D) An organization that represents volunteer firefighters. (E) An organization that represents fire chiefs. (3) Minimum standard The final motor vehicle standard described in paragraph (1) shall require any new electric or hybrid vehicle manufactured for sale, sold, offered for sale, or introduced or delivered for introduction in interstate commerce in the United States to be equipped, at a minimum, with\u2014 (A) first responder access technology that allows immediate access to the battery for purposes of timely extinguishment of an electric vehicle or hybrid vehicle battery fire; (B) technology that suppresses thermal runaway if an electric vehicle or hybrid vehicle battery cell is damaged; (C) safeguards to delay breaching of the passenger compartment by an electric vehicle or hybrid vehicle battery fire, sufficient to permit escape or rescue of the vehicle operator and all passengers within a reasonable period of time from a collision or battery malfunction; and (D) battery and first responder access placed in uniform, standardized locations within the vehicle, subject to industry standards, in order to assist firefighters in recognizing and responding to battery fires. (4) Guidance for firefighters Not later than 1 year after the promulgation of the final motor vehicle standard described in paragraph (1), the Secretary shall publish guidance on responding to fire incidents involving batteries used in electric vehicles and hybrid vehicles to be used as the basis for training firefighters. (b) Mechanical door release Not later than 2 years after the date of the enactment of this section, the Secretary shall promulgate a final motor vehicle safety standard that requires any new electric vehicle or hybrid vehicle manufactured for sale, sold, offered for sale, or introduced or delivered for introduction in interstate commerce in the United States to have clearly marked interior and exterior mechanical door releases on each door and hatch that allows safe exit of such vehicle in case of failure of the electric system of such vehicle. (c) Definitions In this section: (1) Electric vehicle The term electric vehicle means a passenger motor vehicle that is propelled by an electric motor drawing current from a rechargeable storage battery, fuel cell, or other portable source of electrical current, which may include a nonelectrical source of power designed to charge any such battery and component thereof. (2) Hybrid vehicle The term hybrid vehicle means a passenger motor vehicle propelled by a combination of an electric motor and an internal combustion engine or other power source and component thereof. (3) Secretary The term Secretary means the Secretary of Transportation. .\n##### (b) Civil penalty\nSection 30165(a)(1) of such title is amended by inserting 30130, after 30127, .\n##### (c) Clerical amendment\nThe table of sections for subchapter II of chapter 301 of title 49, United States Code, is amended by adding at the end the following:\nSec. 30130. Electric and hybrid vehicles .\n##### (d) Application\nThe amendments made by this Act shall apply to each new electric vehicle or hybrid vehicle manufactured for sale, sold, offered for sale, or introduced or delivered for introduction in interstate commerce in the United States on and after the date that is 2 years after the date on which the Secretary promulgates the final motor vehicle safety standard pursuant to section 30130(a) of title 49, United States Code (as added by subsection (a)).\n#### 2. Study on the health impacts of electric and hybrid vehicle battery fires on first responders\n##### (a) Study\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Health and Human Services shall conduct a study on the health effects of electric and hybrid vehicle battery fires on first responders.\n##### (b) Report\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Health and Human Services shall submit to Congress, and make publicly available on the website of the Department of Health and Human Services, a report that includes the following:\n**(1)**\nThe findings of the study under subsection (a).\n**(2)**\nInput from at least one representative from the following:\n**(A)**\nAn accredited standards development organization with expertise in fire protection.\n**(B)**\nAn organization that represents professional firefighters.\n**(C)**\nAn organization that represents volunteer firefighters.\n**(D)**\nAn organization that represents fire chiefs.\n**(3)**\nRecommendations for legislative action to protect first responders from the health effects of electric and hybrid vehicle battery fires and improve the safety of electric and hybrid vehicle batteries.",
      "versionDate": "2026-01-06",
      "versionType": "Introduced in House"
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
        "name": "Energy",
        "updateDate": "2026-01-22T16:04:10Z"
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
      "date": "2026-01-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6948ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to require each new electric and hybrid vehicle to be equipped with technology that allows the timely extinguishment of an electric vehicle battery fire, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T11:03:19Z"
    },
    {
      "title": "To amend title 49, United States Code, to require each new electric and hybrid vehicle to be equipped with technology that allows the timely extinguishment of an electric vehicle battery fire, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-07T09:05:46Z"
    }
  ]
}
```
